import axios from 'axios'
import useSWR from 'swr'
import Head from 'next/head'
import Link from 'next/link'

const fetcher = url => axios.get(url).then(res => res.data)

export default function Home() {
  const { data, error } = useSWR('http://localhost:8000/apiv1/', fetcher)
  if (!data && !error) {
    return (
      <div>Please wait for a moment...</div>
    )
  }
  if (error) return <div>failed to load</div>
  return (
    <div className='antialiased'>
      <Head>
        <title>Musical Works Lab</title>
        <meta name="description" content="Musical composition metadata" />
        {/* <link rel="icon" href="/favicon.ico" /> */}
      </Head>
      <header className='bg-white shadow py-2 px-10 fixed top-0 w-full'>
        <nav className='flex items-center justify-between'>
          <div>
            {/* Logo */}
            <Link href='/'>
              <h1 className='text-5xl font-extrabold'>
                <span className="bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-violet-500">
                  Musical Works
                </span>
              </h1>
            </Link>
          </div>
          <div className='flex items-center space-x-4'>
            <button className='px-4 rounded-md text-gray-600 border text-[small] font-medium capitalize'>help</button>
            <button className='px-4 rounded-md text-gray-600 border text-[small] font-medium capitalize'>search</button>
            <button className='px-4 rounded-md text-white bg-gradient-to-tr from-pink-400 to-rose-600 via-red-600 text-[small] font-medium'>log in</button>

          </div>
        </nav>
      </header>
      <div className='px-10 h-96 mt-12 bg-gradient-to-br from-pink-600 to-indigo-600 via-rose-600 flex flex-col items-center justify-center'>
        <div className='flex items-center justify-between'>
          <div>
            <h1 className='text-white text-5xl font-semibold'>Indulge yourself in good music.</h1>
          </div>
          <div>
            {/* <img src='music.jpg' className=' object-cover w-1/2 rounded-2xl shadow-xl ' /> */}
          </div>
        </div>
      </div>
    </div>
  )
}
