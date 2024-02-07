import { useState } from 'react'
import axios from 'axios';

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
            <div>ID: {id}</div>
            {isEditing ? (
                <>
                    <input
                        type="text"
                        name="title"
                        value={editedTitle}
                        onChange={handleInputChange}
                    />
                    <input
                        type="text"
                        name="description"
                        value={editedDescription}
                        onChange={handleInputChange}
                    />
                    <button onClick={handleSaveClick}>Save</button>
                </>
            ) : (
                <>
                    <div>Title: {editedTitle}</div>
                    <div>Description: {editedDescription}</div>
                    <button onClick={handleEditClick}>Edit</button>
                    <button onClick={handleDeleteButton}>Delete</button>
                </>
            )}
        </div>
    );
}

export default Task;
