import React, { useState } from 'react';
import axios from 'axios';

 function Registration () {
    const [user, setUser] = useState (
        {
            first_name : '',
            last_name :'',
            email : '',
            username : '',
            password : '',
        }
    );
    const handleChange = (e) => {
        setUser ({
            ...user , 
            [e.target.name]: e.target.value
        });
    }
    const handleSubmit = async(e) => {
        e.preventDefault ();  

        try {
            const response = await axios.post  ('http://localhost:8000/register/',user);
            console.log(response.data);
            if (response.status === 200)
            {
                window.location.href = '/login';                
            }
        }
        catch (error) {
            console.log(error);
        }
    }
    return (
        <form onSubmit = {handleSubmit}>
            <input type = "text" name = "first_name" placeholder = "First Name" onChange={handleChange} />
            <input type = "text" name = "last_name" placeholder = "Last Name" onChange={handleChange} />
            <input type = "email" name = "email" placeholder = "Email" onChange={handleChange} />
            <input type = "text" name = "username" placeholder = "Username" onChange={handleChange} />
            <input type = "text" name = "password" placeholder = "Password" onChange={handleChange} />

            <button type = "Submit"></button>
        </form>
    )
}
export default Registration