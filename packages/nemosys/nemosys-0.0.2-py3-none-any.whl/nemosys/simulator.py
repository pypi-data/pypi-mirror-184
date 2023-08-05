"""
nemosys-simulator
"""

import os
import time
from ctypes import *


class Simulator:
    def __init__(self, path='C:/Simone/Simone-V6_35'):
        self.cwd = os.getcwd()
        self.api = CDLL(f'{path}/exe/simone_api.dll')
        self._set_errcheck()
        self._initialize_api(path)

        self.obj_param_dict = {
            1: [10, 15, 27, 28, 29, 34, 35, 78, 79, 81, 109, 112, 116],
            2: [10, 28, 29, 78, 78, 79, 106],
            4: [40, 41, 105],
            16: [10],
            128: [4, 46, 60, 104, 536936576, 537002112],
            256: [60, 104],
            1024: [],
            524288: [85]}
        self.obj_var_dict = {
            1: [9, 10, 31, 32, 33, 62, 63],
            2: [9, 10, 31, 32, 33, 62, 63],
            4: [9, 31, 32, 33, 62, 63],
            16: [10, 79, 106],
            128: [-1877999605, 3, 8, 536936576, 537002112],
            256: [-1877999605, 3],
            1024: [],
            524288: []}
        self.str_to_extid_dict = {
            'BP': 78,
            'MAX': 77,
            'OFF': 79,
            'ON': 106,
            'PO': 33}

    @staticmethod
    def _bytes(string):
        return bytes(string, 'gbk')

    @staticmethod
    def _validate_result(result, func, arguments):
        if result == 0:
            return None
        else:
            raise SimoneError(result, func, arguments)

    def _set_errcheck(self):
        self.api.simone_init.errcheck = self._validate_result
        self.api.simone_select.errcheck = self._validate_result
        self.api.simone_open.errcheck = self._validate_result
        self.api.simone_close.errcheck = self._validate_result
        self.api.simone_remove.errcheck = self._validate_result
        self.api.simone_execute.errcheck = self._validate_result
        self.api.simone_set_simulation_defaults.errcheck = self._validate_result
        self.api.simone_set_properties.errcheck = self._validate_result
        self.api.simone_set_times.errcheck = self._validate_result
        self.api.simone_write.errcheck = self._validate_result
        self.api.simone_write_ex.errcheck = self._validate_result
        self.api.simone_write_configuration.errcheck = self._validate_result
        return None

    # initialize api
    def _initialize_api(self, path):
        self.api.simone_init(self._bytes(f'{path}/sys/{os.environ["USERNAME"]}_'
                                         f'{os.environ["COMPUTERNAME"]}.ini'))
        return None

    # ops-scenario
    def new_scenario(self, net, sce):
        self.api.simone_select(self._bytes(net))

        if not self.api.simone_open(self._bytes(sce), 3):
            self.api.simone_close()
            self.api.simone_remove(self._bytes(sce), 0)

        self.api.simone_open(self._bytes(sce), 1 | 0x00010000)
        self.api.simone_set_simulation_defaults()
        self.api.simone_set_properties(3, 0, self._bytes('INIT'))
        self.api.simone_set_times(int(time.time()), int(time.time()) + 3600)
        return None

    def open_scenario(self, net, sce):
        self.api.simone_select(self._bytes(net))
        self.api.simone_open(self._bytes(sce), 3)
        return None

    def remove_scenario(self, net, sce):
        self.api.simone_select(self._bytes(net))
        self.api.simone_remove(self._bytes(sce), 0)
        return None

    def execute_scenario(self):
        self.api.simone_execute(c_char_p(self._bytes('.' * 80)), 80)
        self.api.simone_close()
        return None

    # ops-misc
    def list_networks(self):
        net_list = []
        msg = c_char_p(self._bytes('.' * 80))

        self.api.simone_network_list_start(0)

        while True:
            if not self.api.simone_network_list_next(msg, 80):
                net_list.append(msg.value.decode('ascii'))
            else:
                break
        return net_list

    def list_scenarios(self, net):
        sce_list = []
        msg = c_char_p(self._bytes('.' * 80))

        self.api.simone_select(self._bytes(net))
        self.api.simone_scenario_list_start(0)

        while True:
            if not self.api.simone_scenario_list_next(msg, 80):
                sce_list.append(msg.value.decode('ascii'))
            else:
                break
        return sce_list

    def get_extname(self, extid):
        ptr_extname = c_char_p(self._bytes('.' * 80))
        self.api.simone_extid2name(extid, self._bytes('.' * 80), 0)
        return ptr_extname.value

    def get_extid(self, extname):
        extid = c_int()
        ptr_extid = pointer(extid)
        self.api.simone_extname2id(self._bytes(extname), ptr_extid, 0)
        return extid.value

    # i/o-data
    def read_scenario_data(self, net, sce):
        self.open_scenario(net, sce)

        data_msg = self._read_message_data()
        data_obj = self._read_object_data()

        self.api.simone_close()
        return data_msg, data_obj

    def _read_message_data(self):
        msg = c_char_p(self._bytes('.' * 80))
        status = self.api.simone_get_first_message(msg, 80,
                                                   pointer(c_longlong()),
                                                   pointer(c_int()),
                                                   0, 0, 0, 0)

        data_msg = {}
        i = 0
        while not status:
            if i == 0:
                data_msg['run_flag'] = msg.value.decode('ascii')
            else:
                data_msg['line' + str(i)] = msg.value.decode('ascii')

            status = self.api.simone_get_next_message(msg, 80,
                                                      pointer(c_longlong()),
                                                      pointer(c_int()),
                                                      0, 0, 0, 0)
            i += 1
        return data_msg

    def _read_object_data(self):
        objects = []

        obj_id = c_int()
        ptr_id = pointer(obj_id)
        obj_name = c_char_p(self._bytes('.' * 80))
        obj_type = c_int()
        ptr_type = pointer(obj_type)
        obj_subsys = c_char_p(self._bytes('.' * 80))

        status = self.api.simone_get_first_object(-1, 0, ptr_id, obj_name, 80,
                                                  ptr_type, obj_subsys, 80)

        while not status:
            objects.append({'object_id': obj_id.value,
                            'object_name': obj_name.value.decode('ascii'),
                            'object_type': obj_type.value})

            obj_id = c_int()
            ptr_id = pointer(obj_id)
            obj_name = c_char_p(self._bytes('.' * 80))
            obj_type = c_int()
            ptr_type = pointer(obj_type)
            obj_subsys = c_char_p(self._bytes('.' * 80))

            status = self.api.simone_get_next_object(ptr_id, obj_name, 80,
                                                     ptr_type, obj_subsys, 80)

        data_obj = []
        for obj in objects:
            if obj['object_type'] not in self.obj_param_dict.keys():
                continue
            obj['parameter_ids'] = []
            obj['parameter_values'] = []
            obj['parameter_string_ids'] = []
            obj['parameter_string_values'] = []
            obj['variable_ids'] = []
            obj['variable_values'] = []
            obj['variable_string_ids'] = []
            obj['variable_string_values'] = []

            for param_extid in self.obj_param_dict[obj['object_type']]:
                obj_value = c_float()
                ptr_value = pointer(obj_value)
                status = self.api.simone_read(obj['object_id'], param_extid, 0,
                                              ptr_value)
                if status == 0:
                    obj['parameter_ids'].append(param_extid)
                    obj['parameter_values'].append(obj_value.value)
                elif status == 11:
                    obj_param_value = c_char_p(self._bytes('.' * 80))
                    self.api.simone_read_str(obj['object_id'], param_extid, 0,
                                             obj_param_value, 20, 2)
                    obj['parameter_string_ids'].append(param_extid)
                    obj['parameter_string_values'].append(
                        obj_param_value.value.decode('ascii'))
                else:
                    pass

            for var_extid in self.obj_var_dict[obj['object_type']]:
                obj_value = c_float()
                ptr_value = pointer(obj_value)
                status = self.api.simone_read(obj['object_id'], var_extid, 0,
                                              ptr_value)
                if status == 0:
                    obj['variable_ids'].append(var_extid)
                    obj['variable_values'].append(obj_value.value)
                elif status == 11:
                    obj_var_value = c_char_p(self._bytes('.' * 80))
                    self.api.simone_read_str(obj['object_id'], var_extid, 0,
                                             obj_var_value, 20, 2)
                    obj['variable_string_ids'].append(var_extid)
                    obj['variable_string_values'].append(
                        obj_var_value.value.decode('ascii'))
                else:
                    pass

            data_obj.append(obj)
        return data_obj

    def write_scenario_data(self, data_obj):
        for obj in data_obj:
            if obj['object_type'] not in self.obj_param_dict.keys():
                continue

            param_dict = dict(zip(obj['parameter_ids'],
                                  obj['parameter_values']))

            for key in param_dict.keys():
                if param_dict[key] == 0:
                    continue

                if key in [4, 27]:
                    self.api.simone_write_ex(
                        0, obj['object_id'], key, 0, 0,
                        c_float(param_dict[key]), 0, 7, 0, 0, 0, 0)
                elif key in [46, 28, 29]:
                    self.api.simone_write_ex(
                        0, obj['object_id'], key, 0, 0,
                        c_float(param_dict[key]), 0, 14, 0, 0, 0, 0)
                else:
                    self.api.simone_write_ex(
                        0, obj['object_id'], key, 0, 0,
                        c_float(param_dict[key]), 0, 0, 0, 0, 0, 0)

            param_str_dict = dict(zip(obj['parameter_string_ids'],
                                      obj['parameter_string_values']))

            for key in param_str_dict.keys():
                if key == 85:
                    qt_value = 1.0 if param_str_dict[key] == 'ON' else 0.0
                    self.api.simone_write(0, obj['object_id'], key,
                                          c_float(qt_value), 0)
                elif key == 15:
                    self.api.simone_write_configuration(
                        0, obj['object_id'], key,
                        self._bytes(param_str_dict[key]))
                elif key == 10:
                    if param_str_dict[key] not in self.str_to_extid_dict.keys():
                        continue
                    extid_value = self.str_to_extid_dict[param_str_dict[key]]
                    self.api.simone_write(0, obj['object_id'], int(extid_value),
                                          c_float(0.0), 0)
                else:
                    self.api.simone_write_ex(
                        0, obj['object_id'], key, 0, c_float(0.0), 0,
                        self._bytes(param_str_dict[key]),
                        0, c_float(0.0), 0, c_float(0.0), 0)
        return None

    def _write_node_config(self, data_obj, sce_param):
        for obj in data_obj:
            if obj['object_type'] not in self.obj_param_dict.keys():
                continue

            # write demand
            if obj['object_type'] == 256:
                # QSET
                if 4 not in obj['parameter_ids']:
                    obj['parameter_ids'] += [4]
                    obj['parameter_values'] += [sce_param.loc[obj['object_id']]]
                else:
                    idx = obj['parameter_ids'].index(4)
                    obj['parameter_values'][idx] = \
                        sce_param.loc[obj['object_id']]

            # write supply
            elif obj['object_type'] == 128:
                # QSET
                if 4 not in obj['parameter_ids']:
                    obj['parameter_ids'] += [4]
                    obj['parameter_values'] += [sce_param.loc[obj['object_id']]]
                else:
                    idx = obj['parameter_ids'].index(4)
                    obj['parameter_values'][idx] = \
                        sce_param.loc[obj['object_id']]
                # PSET
                if 46 not in obj['parameter_ids']:
                    obj['parameter_ids'] += [46]
                    obj['parameter_values'] += [70.0]
                else:
                    idx = obj['parameter_ids'].index(46)
                    obj['parameter_values'][idx] = 70.0
                # MAXQP
                if 48 not in obj['parameter_ids']:
                    obj['parameter_ids'] += [48]
                    obj['parameter_values'] += [1.0]
                else:
                    idx = obj['parameter_ids'].index(48)
                    obj['parameter_values'][idx] = 1.0
            else:
                pass
        return data_obj

    def _write_valve_config(self, data_obj):
        pipe = []
        valve = []
        for obj in data_obj:
            if obj['object_type'] not in self.obj_param_dict.keys():
                continue

            if obj['object_type'] == 4 and 'CS' in obj['object_name']:
                pipe.append(obj)

        for obj in pipe:
            pos = [i for i in range(len(obj['object_name']))
                   if obj['object_name'].startswith('CS', i)]
            for j in pos:
                key = obj['object_name'][j:j + 7]

                if obj['variable_values'][obj['variable_ids'].index(9)] >= 0:
                    if j == 0:
                        valve.append(key + '_OUT')
                    else:
                        valve.append(key + '_IN')
                else:
                    if j == 0:
                        valve.append(key + '_IN')
                    else:
                        valve.append(key + '_OUT')

        for obj in data_obj:
            if 'CS' not in obj['object_name']:
                continue

            if obj['object_type'] == 16 and obj['object_name'] not in valve:
                # MODE
                if 10 not in obj['parameter_string_ids']:
                    obj['parameter_string_ids'] += [10]
                    obj['parameter_string_values'] += ['OFF']
                else:
                    idx = obj['parameter_string_ids'].index(10)
                    obj['parameter_string_values'][idx] = 'OFF'
            else:
                pass
        return data_obj

    def _write_compressor_config(self, data_obj, factor=1.0):
        for obj in data_obj:
            if obj['object_type'] not in self.obj_param_dict.keys():
                continue

            if obj['object_type'] == 1:
                # CONF
                if 10 not in obj['parameter_string_ids']:
                    obj['parameter_string_ids'] += [10]
                    obj['parameter_string_values'] += ['MAX']
                else:
                    idx = obj['parameter_string_ids'].index(10)
                    obj['parameter_string_values'][idx] = 'MAX'
                # MODE
                if 15 not in obj['parameter_string_ids']:
                    obj['parameter_string_ids'] += [15]
                    obj['parameter_string_values'] += ['FREE']
                else:
                    idx = obj['parameter_string_ids'].index(15)
                    obj['parameter_string_values'][idx] = 'FREE'
                # MMAX
                if 27 not in obj['parameter_ids']:
                    obj['parameter_ids'] += [109]
                    obj['parameter_values'] += \
                        [obj['variable_values'][obj['variable_ids'].index(9)]
                         * (factor + 0.05)]
                else:
                    idx = obj['parameter_ids'].index(109)
                    obj['parameter_values'][idx] = \
                        obj['variable_values'][obj['variable_ids'].index(9)] \
                        * (factor + 0.05)
                # PIMIN
                if 34 not in obj['parameter_ids']:
                    obj['parameter_ids'] += [34]
                    obj['parameter_values'] += [42.0]
                else:
                    idx = obj['parameter_ids'].index(34)
                    obj['parameter_values'][idx] = 42.0
                # POMAX
                if 35 not in obj['parameter_ids']:
                    obj['parameter_ids'] += [35]
                    obj['parameter_values'] += [80.0]
                else:
                    idx = obj['parameter_ids'].index(35)
                    obj['parameter_values'][idx] = 80.0
            else:
                pass
        return data_obj

    # simulation
    def run_config_scenario(self, net, sce_param):
        # run config scenario without parameters
        self.new_scenario(net, 'config')
        self.execute_scenario()
        _, data_obj = self.read_scenario_data(net, 'config')

        # run config scenario with node parameters
        self.new_scenario(net, 'config')
        data_obj = self._write_node_config(data_obj, sce_param)
        self.write_scenario_data(data_obj)
        self.execute_scenario()
        _, data_obj = self.read_scenario_data(net, 'config')

        # run config scenario with node/valve parameters
        self.new_scenario(net, 'config')
        data_obj = self._write_node_config(data_obj, sce_param)
        data_obj = self._write_valve_config(data_obj)
        self.write_scenario_data(data_obj)
        self.execute_scenario()
        data_msg, data_obj = self.read_scenario_data(net, 'config')
        return data_msg, data_obj

    def run_scenario(self, net, sce, sce_config, sce_param, factor):
        self.new_scenario(net, sce)

        # write scenario parameters
        data_obj = self._write_node_config(sce_config, sce_param)
        data_obj = self._write_valve_config(data_obj)
        data_obj = self._write_compressor_config(data_obj, factor)
        self.write_scenario_data(data_obj)

        # execute scenario
        self.execute_scenario()

        # read scenario data
        data_msg, data_obj = self.read_scenario_data(net, sce)
        return data_msg, data_obj

    # exit
    def exit_simone(self):
        self.api.simone_end()
        os.chdir(self.cwd)
        return None


class SimoneError(Exception):
    def __init__(self, result, func, arguments):
        self.result = result
        self.func = func
        self.arguments = arguments
        self.message = self._evaluate_result()

    def __str__(self):
        return f'[{self.func.__name__}{self.arguments}] -> {self.message}'

    def _evaluate_result(self):
        if self.result == 1:
            return 'wrong sequence'
        elif self.result == 2:
            return 'network or scenario not existing'
        elif self.result == 3:
            return 'ID invalid'
        elif self.result == 4:
            return 'timestamp invalid'
        elif self.result == 5:
            return 'parameter(s) invalid'
        elif self.result == 6:
            return 'no valid value'
        elif self.result == 7:
            return 'no licence'
        elif self.result == 8:
            return 'internal error'
        elif self.result == 9:
            return 'no matching entry found'
        elif self.result == 10:
            return 'error getting lock for network or scenario or ' \
                   'another application writes to network or scenario'
        elif self.result == 11:
            return 'value cannot be represented as a float'
        elif self.result == 12:
            return 'calculation failed (simone_execute); ' \
                   'execution of batch failed (SIMONE API extensions)'
        elif self.result == 13:
            return 'an unknown exception has occured'
        elif self.result == 14:
            return 'a remote api call has failed to contact the API Server'
        elif self.result == 15:
            return 'call not implemented in current environment local/remote'
        elif self.result == 16:
            return 'insufficient license level'
        elif self.result == 17:
            return 'no cycle control defined'
        elif self.result == 18:
            return 'incompatible versions'
        elif self.result == 19:
            return 'invalid function definition'
        elif self.result == 20:
            return 'object creation failed due to capacity restrictions'
        else:
            return 'non-specified error'
