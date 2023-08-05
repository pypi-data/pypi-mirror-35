from pathlib import Path
from subprocess import call

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
        resources_path.mkdir()
        source_path.touch()

        with open(str(rc_path), "r") as f:
            data = f.read()
        if "PROMPT_COMMAND" not in data:
            marker = "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> OTHER END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙"
            with open(str(rc_path), "w") as f:
                data = data.replace(f"\n\n{marker}", f"PROMPT_COMMAND='source {str(source_path)};echo '' > {str(source_path)}'\n\n{marker}")
                f.write(data)




