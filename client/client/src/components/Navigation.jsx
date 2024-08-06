import {Link} from 'react-router-dom' 
 
export function Navigation() {
    return (
    <div className='flex justify-between py-3'>
        
        <Link to='/tasks'>
            <h1 className='fond-bold text-3xl mb-4'>TASK APP</h1>
        </Link>  {/*Subtitutes the "a" tag*/}

        <button className='bg-indigo-500 px-3 py-2 rounded-lg'>
            <Link to='/task-create'>
            Create task
            </Link>  {/*Subtitutes the "a" tag*/}
        </button>

    </div>
    )
}