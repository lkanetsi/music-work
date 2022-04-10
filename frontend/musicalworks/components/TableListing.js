import axios from 'axios'
import useSWR from 'swr'

const fetcher = url => axios.get(url).then(res => res.data)

export default function TableListing() {
    const { data, error } = useSWR('http://localhost:8000/apiv1/', fetcher)
    if (!data && !error) {
        return (
            <div className='mt-5 contianer mx-auto w-4/5 text-blue-600 flex flex-col items-center'>Please wait for a moment...</div>
        )
    }
    if (error) return <div className='contianer mx-auto w-4/5 text-rose-600 px-10 py-20 text-bold'>failed to load, please make sure that your django localhost:8000 server is running </div>
    return (
        <div className='mt-5 contianer mx-auto w-4/5 '>
            <table className="table-auto w-full  border-collapse rounded-md border border-slate-100 shadow">
                <thead className='bg-slate-50'>
                    <tr>
                        <th className=' text-left'>Title</th>
                        <th className=' text-left'>Contributors</th>
                        <th className=' text-left'>ISWC</th>
                        <th className=' text-left'>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {data.results.map((music, index) =>
                        <tr key={index} className='text-sm py-2'>
                            <td>{music.title}</td>
                            <td>{music.contributors}</td>
                            <td>{music.iswc}</td>
                            <td>
                                <button className='text-xs px-2 bg-indigo-700 text-white rounded-full font-medium'>view more</button>
                            </td>
                        </tr>
                    )}

                </tbody>
            </table>
        </div>
    )
}
