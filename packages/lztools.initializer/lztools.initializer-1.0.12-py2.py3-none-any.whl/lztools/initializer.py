from pathlib import Path
from subprocess import call
from lztools.git import clone_repo_on_id
from lztools.TempPath import TempPath

home_path = Path.home().absolute()
tool_path = home_path.joinpath(".lztools").absolute()
rc_path = home_path.joinpath(".bashrc")
resources_path = tool_path.joinpath("resources")
source_path = tool_path.joinpath("sourcing")

def is_initializd():
    return tool_path.exists()

def initialize(override=False):
    if override:
        call(["rm", "-rf", str(tool_path)])
    if not is_initializd():
        tool_path.mkdir()
        with TempPath(tool_path.absolute()):
            clone_repo_on_id("Resources")
        source_path.touch()

        with open(str(rc_path), "r") as f:
            data = f.read()
        if "PROMPT_COMMAND" not in data:
            marker = "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> OTHER END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙"
            with open(str(rc_path), "w") as f:
                p = str(source_path)
                data = data.replace(f"\n\n{marker}", f"\nPROMPT_COMMAND='source {p};echo \"\" > {p}'\n\n{marker}")
                f.write(data)


