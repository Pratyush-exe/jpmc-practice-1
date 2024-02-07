import { useState } from 'react'
import axios from 'axios';
import "./Task.css"
import React from 'react'

function Task({ id, title, description, setReload, reload }) {
    const [isEditing, setIsEditing] = useState(false);
    const [editedTitle, setEditedTitle] = useState(title);
    const [editedDescription, setEditedDescription] = useState(description);

    const handleEditClick = () => {
        setIsEditing(true);
    };

    const handleSaveClick = async () => {
        try {
            const data = {
                title: editedTitle,
                description: editedDescription
            };

            const config = {
                headers: {
                    'Content-Type': 'application/json'
                }
            };
            await axios.put('http://localhost:5000/todo/v1/update-task/' + id, data, config);
        } catch (error) {
            console.error('Error Updating data:', error);
        }
        setIsEditing(false);
    };

    const handleCancelClick = () => {
        setIsEditing(false);
        window.location.reload();
    }

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        if (name === 'title') {
            setEditedTitle(value);
        } else if (name === 'description') {
            setEditedDescription(value);
        }
    };

    const handleDeleteButton = async () => {
        await axios.delete('http://localhost:5000/todo/v1/delete-task/' + id);
        setReload(!reload)
        window.location.reload();
    }

    return (
        <div className="task">
            {isEditing ? (
                <div className='edit-cont'>
                    <div className='edit-input'>
                        <input
                            type="text"
                            name="title"
                            value={editedTitle}
                            onChange={handleInputChange}
                            className='title'
                        />
                        <input
                            type="text"
                            name="description"
                            value={editedDescription}
                            onChange={handleInputChange}
                        />
                    </div>
                    <div className='edit-input'>
                        <button onClick={handleSaveClick}>Save</button>
                        <button onClick={handleCancelClick}>Cancel</button>
                    </div>
                </div>
            ) : (
                <div className='display-cont'>
                    <div className='display-div'>
                        <div className='title' style={{ margin: '5px' }}>{editedTitle}</div>
                        <div className='description' style={{ margin: '5px' }}>{editedDescription}</div>
                    </div>
                    <div className='display-buttons'>
                        <button onClick={handleEditClick}>Edit</button>
                        <button onClick={handleDeleteButton}>Delete</button>
                    </div>
                </div>
            )}
        </div>
    );
}

export default Task;
