<a id="camel.tasks.task"></a>

<a id="camel.tasks.task.TaskValidationMode"></a>

## TaskValidationMode

```python
class TaskValidationMode(Enum):
```

Validation modes for different use cases.

<a id="camel.tasks.task.validate_task_content"></a>

## validate_task_content

```python
def validate_task_content(
    content: str,
    task_id: str = 'unknown',
    min_length: int = 1,
    mode: TaskValidationMode = TaskValidationMode.INPUT,
    check_failure_patterns: bool = True
):
```

Unified validation for task content and results to avoid silent
failures. Performs comprehensive checks to ensure content meets quality
standards.

**Parameters:**

- **content** (str): The task content or result to validate.
- **task_id** (str): Task ID for logging purposes. (default: :obj:`"unknown"`)
- **min_length** (int): Minimum content length after stripping whitespace. (default: :obj:`1`)
- **mode** (TaskValidationMode): Validation mode - INPUT for task content, OUTPUT for task results. (default: :obj:`TaskValidationMode.INPUT`)
- **check_failure_patterns** (bool): Whether to check for failure indicators in the content. Only effective in OUTPUT mode. (default: :obj:`True`)

**Returns:**

  bool: True if content passes validation, False otherwise.

<a id="camel.tasks.task.is_task_result_insufficient"></a>

## is_task_result_insufficient

```python
def is_task_result_insufficient(task: 'Task'):
```

Check if a task result is insufficient and should be treated as failed.

This is a convenience wrapper around validate_task_content for backward
compatibility and semantic clarity when checking task results.

**Parameters:**

- **task** (Task): The task to check.

**Returns:**

  bool: True if the result is insufficient, False otherwise.

<a id="camel.tasks.task.parse_response"></a>

## parse_response

```python
def parse_response(response: str, task_id: Optional[str] = None):
```

Parse Tasks from a response.

**Parameters:**

- **response** (str): The model response.
- **task_id** (str, optional): a parent task id, the default value is "0"

**Returns:**

  List[Task]: A list of tasks which is :obj:`Task` instance.

<a id="camel.tasks.task.TaskState"></a>

## TaskState

```python
class TaskState(str, Enum):
```

<a id="camel.tasks.task.TaskState.states"></a>

### states

```python
def states(cls):
```

<a id="camel.tasks.task.Task"></a>

## Task

```python
class Task(BaseModel):
```

Task is specific assignment that can be passed to a agent.

**Parameters:**

- **content** (str): string content for task.
- **id** (str): An unique string identifier for the task. This should ideally be provided by the provider/model which created the task. (default: :obj:`uuid.uuid4()`)
- **state** (TaskState): The state which should be OPEN, RUNNING, DONE or DELETED. (default: :obj:`TaskState.FAILED`)
- **type** (Optional[str]): task type. (default: :obj:`None`)
- **parent** (Optional[Task]): The parent task, None for root task. (default: :obj:`None`)
- **subtasks** (List[Task]): The childrent sub-tasks for the task. (default: :obj:`[]`)
- **result** (Optional[str]): The answer for the task. (default: :obj:`""`)
- **failure_count** (int): The failure count for the task. (default: :obj:`0`)
- **assigned_worker_id** (Optional[str]): The ID of the worker assigned to this task. (default: :obj:`None`)
- **additional_info** (Optional[Dict[str, Any]]): Additional information for the task. (default: :obj:`None`)
- **image_list** (Optional[List[Image.Image]]): Optional list of PIL Image objects associated with the task. (default: :obj:`None`)
- **image_detail** (`Literal["auto", "low", "high"]`): Detail level of the images associated with the task. (default: :obj:`auto`)
- **video_bytes** (Optional[bytes]): Optional bytes of a video associated with the task. (default: :obj:`None`)
- **video_detail** (`Literal["auto", "low", "high"]`): Detail level of the videos associated with the task. (default: :obj:`auto`)

<a id="camel.tasks.task.Task.__repr__"></a>

### __repr__

```python
def __repr__(self):
```

Return a string representation of the task.

<a id="camel.tasks.task.Task.from_message"></a>

### from_message

```python
def from_message(cls, message: BaseMessage):
```

Create a task from a message.

**Parameters:**

- **message** (BaseMessage): The message to the task.

**Returns:**

  Task

<a id="camel.tasks.task.Task.to_message"></a>

### to_message

```python
def to_message():
```

Convert a Task to a Message.

<a id="camel.tasks.task.Task.reset"></a>

### reset

```python
def reset(self):
```

Reset Task to initial state.

<a id="camel.tasks.task.Task.update_result"></a>

### update_result

```python
def update_result(self, result: str):
```

Set task result and mark the task as DONE.

**Parameters:**

- **result** (str): The task result.

<a id="camel.tasks.task.Task.set_id"></a>

### set_id

```python
def set_id(self, id: str):
```

Set the id of the task.

**Parameters:**

- **id** (str): The id of the task.

<a id="camel.tasks.task.Task.set_state"></a>

### set_state

```python
def set_state(self, state: TaskState):
```

Recursively set the state of the task and its subtasks.

**Parameters:**

- **state** (TaskState): The giving state.

<a id="camel.tasks.task.Task.add_subtask"></a>

### add_subtask

```python
def add_subtask(self, task: 'Task'):
```

Add a subtask to the current task.

**Parameters:**

- **task** (Task): The subtask to be added.

<a id="camel.tasks.task.Task.remove_subtask"></a>

### remove_subtask

```python
def remove_subtask(self, id: str):
```

Remove a subtask from the current task.

**Parameters:**

- **id** (str): The id of the subtask to be removed.

<a id="camel.tasks.task.Task.get_running_task"></a>

### get_running_task

```python
def get_running_task(self):
```

Get RUNNING task.

<a id="camel.tasks.task.Task.to_string"></a>

### to_string

```python
def to_string(self, indent: str = '', state: bool = False):
```

Convert task to a string.

**Parameters:**

- **indent** (str): The ident for hierarchical tasks.
- **state** (bool): Include or not task state.

**Returns:**

  str: The printable task string.

<a id="camel.tasks.task.Task.get_result"></a>

### get_result

```python
def get_result(self, indent: str = ''):
```

Get task result to a string.

**Parameters:**

- **indent** (str): The ident for hierarchical tasks.

**Returns:**

  str: The printable task string.

<a id="camel.tasks.task.Task.decompose"></a>

### decompose

```python
def decompose(
    self,
    agent: 'ChatAgent',
    prompt: Optional[str] = None,
    task_parser: Callable[[str, str], List['Task']] = parse_response
):
```

Decompose a task to a list of sub-tasks. Automatically detects
streaming or non-streaming based on agent configuration.

**Parameters:**

- **agent** (ChatAgent): An agent that used to decompose the task.
- **prompt** (str, optional): A prompt to decompose the task. If not provided, the default prompt will be used.
- **task_parser** (Callable[[str, str], List[Task]], optional): A function to extract Task from response. If not provided, the default parse_response will be used.

**Returns:**

  Union[List[Task], Generator[List[Task], None, None]]: If agent is
configured for streaming, returns a generator that yields lists
of new tasks as they are parsed. Otherwise returns a list of
all tasks.

<a id="camel.tasks.task.Task._decompose_streaming"></a>

### _decompose_streaming

```python
def _decompose_streaming(
    self,
    response: 'StreamingChatAgentResponse',
    task_parser: Callable[[str, str], List['Task']]
):
```

Handle streaming response for task decomposition.

**Parameters:**

- **response**: Streaming response from agent
- **task_parser**: Function to parse tasks from response
- **Yields**: List[Task]: New tasks as they are parsed from streaming response

<a id="camel.tasks.task.Task._decompose_non_streaming"></a>

### _decompose_non_streaming

```python
def _decompose_non_streaming(self, response, task_parser: Callable[[str, str], List['Task']]):
```

Handle non-streaming response for task decomposition.

**Parameters:**

- **response**: Regular response from agent
- **task_parser**: Function to parse tasks from response

**Returns:**

  List[Task]: All parsed tasks

<a id="camel.tasks.task.Task._parse_partial_tasks"></a>

### _parse_partial_tasks

```python
def _parse_partial_tasks(self, response: str):
```

Parse tasks from potentially incomplete response.

**Parameters:**

- **response**: Partial response content

**Returns:**

  List[Task]: Tasks parsed from complete `<task>``</task>` blocks

<a id="camel.tasks.task.Task.compose"></a>

### compose

```python
def compose(
    self,
    agent: 'ChatAgent',
    template: TextPrompt = TASK_COMPOSE_PROMPT,
    result_parser: Optional[Callable[[str], str]] = None
):
```

compose task result by the sub-tasks.

**Parameters:**

- **agent** (ChatAgent): An agent that used to compose the task result.
- **template** (TextPrompt, optional): The prompt template to compose task. If not provided, the default template will be used.
- **result_parser** (Callable[[str, str], List[Task]], optional): A function to extract Task from response.

<a id="camel.tasks.task.Task.get_depth"></a>

### get_depth

```python
def get_depth(self):
```

Get current task depth.

<a id="camel.tasks.task.TaskManager"></a>

## TaskManager

```python
class TaskManager:
```

TaskManager is used to manage tasks.

**Parameters:**

- **task** (Task): The root Task.

<a id="camel.tasks.task.TaskManager.__init__"></a>

### __init__

```python
def __init__(self, task: Task):
```

<a id="camel.tasks.task.TaskManager.gen_task_id"></a>

### gen_task_id

```python
def gen_task_id(self):
```

Generate a new task id.

<a id="camel.tasks.task.TaskManager.exist"></a>

### exist

```python
def exist(self, task_id: str):
```

Check if a task with the given id exists.

<a id="camel.tasks.task.TaskManager.current_task"></a>

### current_task

```python
def current_task(self):
```

Get the current task.

<a id="camel.tasks.task.TaskManager.topological_sort"></a>

### topological_sort

```python
def topological_sort(tasks: List[Task]):
```

Sort a list of tasks by topological way.

**Parameters:**

- **tasks** (List[Task]): The giving list of tasks.

**Returns:**

  The sorted list of tasks.

<a id="camel.tasks.task.TaskManager.set_tasks_dependence"></a>

### set_tasks_dependence

```python
def set_tasks_dependence(
    root: Task,
    others: List[Task],
    type: Literal['serial', 'parallel'] = 'parallel'
):
```

Set relationship between root task and other tasks.
Two relationships are currently supported: serial and parallel.
`serial` :  root -> other1 -> other2
`parallel`: root -> other1
-> other2

**Parameters:**

- **root** (Task): A root task.
- **others** (List[Task]): A list of tasks.

<a id="camel.tasks.task.TaskManager.add_tasks"></a>

### add_tasks

```python
def add_tasks(self, tasks: Union[Task, List[Task]]):
```

self.tasks and self.task_map will be updated by the input tasks.

<a id="camel.tasks.task.TaskManager.evolve"></a>

### evolve

```python
def evolve(
    self,
    task: Task,
    agent: 'ChatAgent',
    template: Optional[TextPrompt] = None,
    task_parser: Optional[Callable[[str, str], List[Task]]] = None
):
```

Evolve a task to a new task.
Evolve is only used for data generation.

**Parameters:**

- **task** (Task): A given task.
- **agent** (ChatAgent): An agent that used to evolve the task.
- **template** (TextPrompt, optional): A prompt template to evolve task. If not provided, the default template will be used.
- **task_parser** (Callable, optional): A function to extract Task from response. If not provided, the default parser will be used.

**Returns:**

  Task: The created :obj:`Task` instance or None.
