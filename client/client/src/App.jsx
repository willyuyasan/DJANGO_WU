import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import {TasksPage} from './pages/TaskswuPage'
import {TasksFormPage} from './pages/TaskswuFormPage'
import {Navigation} from './components/Navigation'
import {Toaster} from 'react-hot-toast'

function App() {
  return (
    <BrowserRouter>
    <div className='container mx-auto'>
    <Navigation/>
      <Routes>
        # Directs to the distinct pages
        <Route path='/' element={<Navigate to = '/tasks'/>}/>  # Redirect to a default page
        <Route path='/tasks' element={<TasksPage/>}/>
        <Route path='/task-create' element={<TasksFormPage/>}/>
        <Route path='/task/:id' element={<TasksFormPage/>}/>
      </Routes>
      <Toaster/>
    </div>
    </BrowserRouter>
  )
}

export default App