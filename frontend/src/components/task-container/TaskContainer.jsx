import { useEffect, useState } from "react"
import Task from "../task/Task"
import axios from "axios"


const TaskContainer = () => {
    const [items, setItems] = useState([])
    const [reload, setReload] = useState(false)
    const [newTaskTitle, setNewTaskTitle] = useState("")
    const [newTaskDescription, setNewTaskDescription] = useState("")

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://localhost:5000/todo/v1/get-tasks');
                setItems(response.data['data']);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, [reload]);

    const handleAddTask = async () => {
        try {
            const data = {
                title: newTaskTitle,
                description: newTaskDescription
            };

            const config = {
                headers: {
                    'Content-Type': 'application/json'
                }
            };
            const response = await axios.post('http://localhost:5000/todo/v1/create-task', data, config);
            console.log("Task added:", response.data);
            const updatedResponse = await axios.get('http://localhost:5000/todo/v1/get-tasks');
            setItems(updatedResponse.data['data']);
        } catch (error) {
            console.error('Error adding task:', error);
        }
    };

    return (
        <div className="task-container">
            <div className="add-task">
                <input
                    type="text"
                    placeholder="Enter task title"
                    value={newTaskTitle}
                    onChange={(e) => setNewTaskTitle(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Enter task description"
                    value={newTaskDescription}
                    onChange={(e) => setNewTaskDescription(e.target.value)}
                />
                <button onClick={handleAddTask}>Add Task</button>
            </div>
            <div className="tasks">
                {items.map((x, i) => (
                    <div key={i}>
                        <Task
                            id={x['uuid']}
                            title={x['title']}
                            description={x['description']}
                            setReload={setReload}
                            reload={reload}
                        />
                    </div>
                ))}
            </div>
        </div>
    )
}

export default TaskContainer