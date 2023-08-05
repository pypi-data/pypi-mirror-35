import pytest
import shutil

def test_empty_eda_api():
    import tempfile
    from edalize import get_edatool

    (h, eda_api_file) = tempfile.mkstemp()

    with pytest.raises(RuntimeError):
        backend = get_edatool('icarus')(eda_api_file=eda_api_file)

def test_incomplete_eda_api():
    import tempfile
    import yaml
    from edalize import get_edatool

    (h, eda_api_file) = tempfile.mkstemp()
    contents = []
    
    with open(eda_api_file,'w') as f:
        f.write(yaml.dump({'version' : '0.1.2'}))

    with pytest.raises(RuntimeError) as excinfo:
        backend = get_edatool('icarus')(eda_api_file=eda_api_file)
    assert "Missing required parameter 'name'" in str(excinfo.value)

    with open(eda_api_file,'w') as f:
        f.write(yaml.dump({'version' : '0.1.2',
                           'name' : 'corename'}))

    backend = get_edatool('icarus')(eda_api_file=eda_api_file)

def test_eda_api_files():
    import tempfile
    import yaml

    from edalize import get_edatool
    files = [{'name' : 'plain_file'},
             {'name' : 'subdir/plain_include_file',
              'is_include_file' : True},
             {'name' : 'file_with_args',
              'file_type' : 'verilogSource',
              'logical_name' : 'libx'},
             {'name' : 'include_file_with_args',
              'is_include_file' : True,
              'file_type' : 'verilogSource',
              'logical_name' : 'libx'}]
    (h, eda_api_file) = tempfile.mkstemp(prefix='eda_api_files_')
    with open(eda_api_file,'w') as f:
        f.write(yaml.dump({'files' : files,
                           'name' : 'test_eda_api_files'}))

    backend = get_edatool('icarus')(eda_api_file=eda_api_file)
    (parsed_files, incdirs) = backend._get_fileset_files()

    assert len(parsed_files) == 2
    assert parsed_files[0].name         == 'plain_file'
    assert parsed_files[0].file_type    == ''
    assert parsed_files[0].logical_name == ''
    assert parsed_files[1].name         == 'file_with_args'
    assert parsed_files[1].file_type    == 'verilogSource'
    assert parsed_files[1].logical_name == 'libx'

    assert incdirs == ['subdir', '.']

def test_eda_api_hooks():
    import os.path
    import tempfile
    import yaml
    from edalize import get_edatool

    tests_dir = os.path.dirname(__file__)
    ref_dir   = os.path.join(tests_dir, __name__)

    script = 'exit_1_script'
    hooks = {'pre_build' : [
        {'cmd' : ['sh', os.path.join(ref_dir, script)],
         'name' : script}]}

    (h, eda_api_file) = tempfile.mkstemp(prefix='eda_api_hooks_')
    with open(eda_api_file,'w') as f:
        f.write(yaml.dump({'hooks' : hooks,
                           'name' : script}))

    backend = get_edatool('icarus')(eda_api_file=eda_api_file)
    with pytest.raises(RuntimeError):
        backend.build()
