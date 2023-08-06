data_loader_bash_script = """#!/bin/bash

if [[ $(__lztools_resources has_output) == "True" ]]
then
    out_path="{}"
    source $out_path
    echo '' > $out_path
fi"""