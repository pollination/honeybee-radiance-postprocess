from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs


@dataclass
class DaylightOption1(Function):
    """Calculate credits for LEED v4.1 Daylight Option 1."""

    folder = Inputs.folder(
        description='This folder is an output folder of annual daylight recipe. Folder '
        'should include grids_info.json and sun-up-hours.txt. The command uses the list '
        'in grids_info.json to find the result files for each sensor grid.',
        path='results'
    )

    shade_transmittance = Inputs.float(
        description='', default=0.2
    )

    shade_transmittances = Inputs.file(
        description='Path to an annual schedule file. Values should be 0-1 separated '
        'by new line. If not provided an 8-5 annual schedule will be created.',
        path='shade_transmittance.json', optional=True
    )

    model = Inputs.file(
        description='Path to input HBJSON file.',
        path='model.hbjson', optional=True
    )

    @command
    def leed_daylight_option_1(self):
        return 'honeybee-radiance-postprocess post-process leed daylight_option_1 ' \
            'results --shade-transmittance {{self.shade_transmittance}} ' \
            '--shade-transmittance-file {{self.shade_transmittances}} ' \
            '--sub-folder leed_summary'

    # outputs
    leed_summary = Outputs.folder(
        description='Annual metrics folder. This folder includes all the other '
        'sub-folders which are also exposed as separate outputs.',
        path='leed_summary'
    )
