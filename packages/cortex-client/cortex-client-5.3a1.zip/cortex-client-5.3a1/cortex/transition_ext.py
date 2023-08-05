import os
import types
from ds_discovery import Transition
from ds_discovery.handlers.handler import Handler


def create_save_file(f_type):
    def save_file(tr: Transition, data, tag=None, version="0.00"):
        tag = tag or tr.contract_name
        f_dir = getattr(tr.file_properties, 'dir_%s' % f_type)
        Handler.pickle_dump(data=data, file=os.path.join(f_dir, '%s_%s_v%s.p' % (f_type, tag, version)))
    return save_file


def create_load_file(f_type):
    def load_file(tr: Transition, tag=None, version="0.00"):
        tag = tag or tr.contract_name
        f_dir = getattr(tr.file_properties, 'dir_%s' % f_type)
        return Handler.pickle_load(file=os.path.join(f_dir, '%s_%s_v%s.p' % (f_type, tag, version)))
    return load_file


def create_remove_file(f_type):
    def remove_file(tr: Transition, tag=None, version="0.00"):
        tag = tag or tr.contract_name
        f_dir = getattr(tr.file_properties, 'dir_%s' % f_type)
        file_path = os.path.join(f_dir, '%s_%s_v%s.p' % (f_type, tag, version))
        if os.path.isfile(file_path):
            os.remove(file_path)
    return remove_file


def create_has_file(f_type):
    def has_file(tr: Transition, tag=None, version="0.00"):
        tag = tag or tr.contract_name
        f_dir = getattr(tr.file_properties, 'dir_%s' % f_type)
        file_path = os.path.join(f_dir, '%s_%s_v%s.p' % (f_type, tag, version))
        return os.path.isfile(file_path)
    return has_file


def set_auto_cleaners(tr: Transition, df):
    tr.set_cleaner(tr.clean.clean_header(df, inplace=True))
    tr.set_cleaner(tr.clean.auto_remove_columns(df, inplace=True))
    tr.set_cleaner(tr.clean.auto_to_category(df, inplace=True))


def patch_tr(tr: Transition):
    tr.save_raw_file = types.MethodType(create_save_file('raw'), tr)
    tr.load_raw_file = types.MethodType(create_load_file('raw'), tr)
    tr.remove_raw_file = types.MethodType(create_remove_file('raw'), tr)
    tr.remove_clean_file = types.MethodType(create_remove_file('clean'), tr)
    tr.has_raw_file = types.MethodType(create_has_file('raw'), tr)
    tr.save_model_file = types.MethodType(create_save_file('model'), tr)
    tr.load_model_file = types.MethodType(create_load_file('model'), tr)
    tr.save_extract_file = types.MethodType(create_save_file('extract'), tr)
    tr.load_extract_file = types.MethodType(create_load_file('extract'), tr)
    tr.save_feature_file = types.MethodType(create_save_file('feature'), tr)
    tr.load_feature_file = types.MethodType(create_load_file('feture'), tr)
    tr.save_train_file = types.MethodType(create_save_file('train'), tr)
    tr.load_train_file = types.MethodType(create_load_file('train'), tr)
    tr.auto_clean = types.MethodType(set_auto_cleaners, tr)
