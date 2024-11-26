from typing import Any, Literal, NotRequired, TypeAlias, TypedDict

from gazu.asset import AssetTypeDict
from gazu.person import PersonDict
from gazu.task import TaskStatusDict, TaskTypeDict

from .client import KitsuClient, default_client

class ProjectDict(TypedDict):
    name: str
    code: str | None
    description: str | None
    shotgun_id: str | None
    file_tree: str | None
    data: None
    has_avatar: bool
    fps: str
    ratio: str
    resolution: str
    production_type: Literal["shots"]
    production_style: Literal["vfx"]
    start_date: str
    end_date: str
    man_days: None
    nb_episodes: int
    episode_span: int
    max_retakes: int
    is_clients_isolated: bool
    is_preview_download_allowed: bool
    is_set_preview_automated: bool
    homepage: Literal["shots", "assets"]
    project_status_id: str
    default_preview_background_file_id: str | None
    team: list[str]
    asset_types: list[str]
    task_statuses: list[str]
    task_types: list[str]
    status_automations: list[str]
    preview_background_files: list[str]
    id: str
    created_at: str
    updated_at: str
    type: Literal["Project"]
    project_status_name: Literal["Open"]

class ProjectDictPartial(TypedDict):
    id: str
    fps: NotRequired[str]
    ratio: NotRequired[str]
    resolution: NotRequired[str]
    homepage: NotRequired[Literal["shots", "assets"]]

ProductionStyle: TypeAlias = Literal[
    "2d",
    "3d",
    "2d3d",
    "ar",
    "vfx",
    "stop-motion",
    "motion-design",
    "archviz",
    "commercial",
    "catalog",
    "immersive",
    "nft",
    "video-game",
    "vr",
]

ProductionType: TypeAlias = Literal["short", "featurefilm", "tvshow"]

_ModelList = list[str] | list[dict[str, Any]]

def get_project(
    project_id: str, client: KitsuClient = default_client
) -> ProjectDict: ...
def get_project_by_name(
    project_name: str, client: KitsuClient = default_client
) -> ProjectDict | None: ...
def new_project(
    name: str,
    production_type: ProductionType = "short",
    team: list[PersonDict] | list[str] = [],
    asset_types: list[AssetTypeDict] | list[str] = [],
    task_statuses: list[TaskStatusDict] | list[str] = [],
    task_types: list[TaskTypeDict] | list[str] = [],
    production_style: ProductionStyle = "2d3d",
    client: KitsuClient = default_client,
) -> ProjectDict: ...
def add_task_status(
    project: str | ProjectDict,
    task_status: str | TaskStatusDict,
    client: KitsuClient = default_client,
) -> ProjectDict: ...
def get_team(
    project: ProjectDict | str, client: KitsuClient = default_client
) -> list[PersonDict]: ...
def update_project(
    project: ProjectDictPartial, client: KitsuClient = default_client
) -> ProjectDict: ...
def add_task_type(
    project: ProjectDict | str,
    task_type: TaskTypeDict,
    priority: int | None,
    client: KitsuClient = default_client,
) -> ProjectDict: ...