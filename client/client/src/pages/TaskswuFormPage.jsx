import {useForm} from 'react-hook-form'
import {createTask, deleteTask, updateTask, obtainTask} from '../api/task.api'
import {useNavigate, useParams} from 'react-router-dom'
import {useEffect} from 'react'
import {toast} from 'react-hot-toast'

export function TasksFormPage() {

    const {register, handleSubmit, formState:{errors}, setValue} = useForm()
    const navigate = useNavigate()
    const params = useParams()
    // console.log(params)
    const onSubmit = handleSubmit(async data => {
        data['user']=1
        console.log(data)
        if (params.id){
            console.log('Updating...')
            console.log(data)
            await updateTask(params.id, data)
        } else {
            const response = await createTask(data)
            console.log(response)
            toast.success('Created task!', {
                position: 'bottom-right',
                style: {
                    background: '#101010',
                    color: '#fff'
                }
            })
        }
        
        navigate('/tasks')
    })

    useEffect(() => {
        async function obtainedTask() {
            if(params.id){
                //console.log('Obtaining params')
                const obtainedtask = await obtainTask(params.id)
                console.log(obtainedtask)
                setValue('tittle',obtainedtask.data.tittle) //filling value into the form
                setValue('description',obtainedtask.data.description) //filling value into the form
            }
        }
        obtainedTask()
    }, [])

    return (
        <div className='max-w-xl mx-auto'>
            Tasks Form wu Page
            <form onSubmit={onSubmit}>
                <input 
                className='bg-zinc-700 p-3 rounded-lg block w-full mb-3'
                type="text" placeholder="tittle"
                {...register("tittle", {required:true})}
                />
                {errors.tittle && <span>This field is required</span>}
                <textarea 
                className='bg-zinc-700 p-3 rounded-lg block w-full mb-3'
                rows="10" placeholder="description"
                {...register("description", {required:true})}
                >
                </textarea>
                {errors.description && <span>This field is required</span>}
                <button
                className='bg-indigo-500 p-3 rounded-lg block w-full mt-3'
                >
                    Save
                </button>
            </form>

            {params.id && (
            <div className='flex justify-end'>
                <button 
                className='bg-red-500 rounded-lg w-48 mt-3'
                onClick= {async () => {
                    const accepted = window.confirm('Are you sure of deleting the task?')
                    if (accepted){
                        await deleteTask(params.id)
                        navigate('/tasks')
                    }
                }}
                >
                Delete
                </button>
            </div>
            )}
            
        </div>
    )
}