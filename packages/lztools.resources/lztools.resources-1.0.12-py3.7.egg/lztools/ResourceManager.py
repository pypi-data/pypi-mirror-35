from pathlib import Path
from subprocess import call

from lztools.TempPath import TempPath
from lztools.git import clone_repo

from lztools.shared_resources import repos
from lztools.shared_resources.strings import data_loader_bash_script

_user_home = Path.home().absolute()
main_path = _user_home .joinpath(".lztools").absolute()
scripts_path = main_path.joinpath("scripts")
loader_path = scripts_path.joinpath("data_loader")
data_path = main_path.joinpath("data")
out_path = data_path.joinpath("out_data")
resources_path = main_path.joinpath("resources")
bashrc_path = _user_home.joinpath(".bashrc")

def ensure_initialized(override=False):
    if override:
        call(["rm", "-rf", str(main_path)])
    if not main_path.exists():
        main_path.mkdir()
        scripts_path.mkdir()
        loader_path.touch()
        data_path.mkdir()
        out_path.touch()
        loader_path.write_text(data_loader_bash_script.format(out_path.absolute()))

        with TempPath(main_path.absolute()):
            clone_repo(repos.Resources)

        data = bashrc_path.read_text()
        if "PROMPT_COMMAND" not in data:
            marker = "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> OTHER END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙"
            data = data.replace(f"\n\n{marker}", f"\nPROMPT_COMMAND='source {str(loader_path)}'\n\n{marker}")
            bashrc_path.write_text(data)