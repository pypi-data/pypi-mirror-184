# Authors: Christoph Dinh <christoph.dinh@brain-link.de>
#          Johannes Behrens <johannes.behrens@brain-link.de>
#          David Schote <david.schote@brain-link.de>
#
# License: BSD-3-Clause

from pydantic import BaseModel, StrictStr

from uuid import UUID


class RecoJob(BaseModel):
    """RecoJob is a pydantic model for a reco job.""" # noqa: E501
    reco_id: StrictStr
    device_id: int | str | UUID
    record_id: int | str | UUID
    input: StrictStr