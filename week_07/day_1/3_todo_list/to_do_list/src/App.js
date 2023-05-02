import './App.css';
import React, {useState} from 'react'

function App() {

  const [tasks, setTasks] = useState([
    { name: "Buy groceries", priority: "low"},
    { name: "Cook dinner", priority: "high" },
    { name: "Wash dishes", priority: "low" },
  ]);
  const [newTask, setNewTask] = useState("");
  const [newPriority, setNewPriority] = useState("");


  const taskNodes = tasks.map((task, index) => {
    return(
      <li key={index} className={task.priority}>
        <span>{ task.name }</span>
      </li>
    );
  });

  const handleTaskInput = (event) => {
    setNewTask(event.target.value);
  };

  const handlePriority = (event) => {
    setNewPriority(event.target.value);
  };

  const saveNewTask = (event) => {
    event.preventDefault();
    const copyTasks = [...tasks];
    copyTasks.push({name: newTask, priority: newPriority});
    setTasks(copyTasks);
    setNewTask("");
    setNewPriority("");
  };


  return (
    <div className="App">

      <h1>ToDo List</h1>
      <hr></hr>

      <form onSubmit={saveNewTask}>
        <label htmlFor="new-task">Add a new task:</label>
        <input id="new-task" type="text" value={newTask} onChange={handleTaskInput}/>
        <input id="high-priority" type="radio" name="priority" value="high" onChange={handlePriority} checked={newPriority === "high"}/>High
        <input id="low-priority" type="radio" name="priority" value="low" onChange={handlePriority} checked={newPriority === "low"}/>Low
        <input type="submit" value="Save New Task" />
      </form>
      <ul>
        {taskNodes}
      </ul>
    </div>
  );
};

export default App;