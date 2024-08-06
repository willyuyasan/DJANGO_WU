import { useEffect, useState} from "react"
import {getAllTask} from '../api/task.api'
import {TaskCard} from '../components/TaskCard'


export function TaskList() {

    const [tasks, setTasks] = useState([])

    useEffect(()=> {
        {/**useEffect is the event for page charge*/}
        console.log('page loaded!')
        
        {/**Calling function of the axios request and storing in a react variable*/}
        async function loadTaskfromapi() {
            const res = await getAllTask() 
            setTasks(res.data)
        }

        loadTaskfromapi()

    }, [])

    return(
        <div className='grid grid-cols-3 gap-3'>
            {tasks.map(task => (<TaskCard task={task} key={task.id}/>))}
        </div>
    )
}