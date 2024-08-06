import axios from 'axios'

const taskApi = axios.create({
    baseURL: 'http://localhost:8001/task/api/v1/tasks/'
})

export const getAllTask = () => taskApi.get('/')
export const createTask = (task) => taskApi.post('/',task)
export const deleteTask = (id) => taskApi.delete(`/${id}`)
export const updateTask = (id, task) => taskApi.put(`/${id}/`, task)
export const obtainTask = (id) => taskApi.get(`/${id}/`)