import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

interface Subject {
  id: number
  name: string
  exam_type: string
}

interface Topic {
  id: number
  title: string
}

interface SubjectWithTopics extends Subject {
  topics: Topic[]
}

export default function Dashboard() {
  const [subjects, setSubjects] = useState<SubjectWithTopics[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchSubjects()
  }, [])

  const fetchSubjects = async () => {
    try {
      const response = await axios.get('/api/subjects')
      const subjectsData = response.data

      // Fetch topics for each subject
      const subjectsWithTopics = await Promise.all(
        subjectsData.map(async (subject: Subject) => {
          try {
            const topicsResponse = await axios.get(`/api/subjects/${subject.id}/topics`)
            return { ...subject, topics: topicsResponse.data }
          } catch (err) {
            return { ...subject, topics: [] }
          }
        })
      )

      setSubjects(subjectsWithTopics)
    } catch (err: any) {
      setError('Failed to load subjects')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="text-center">
        <p className="text-red-600">{error}</p>
        <button
          onClick={fetchSubjects}
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
        >
          Retry
        </button>
      </div>
    )
  }

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <p className="mt-2 text-gray-600">Choose a subject to start studying</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {subjects.map((subject) => (
          <div key={subject.id} className="bg-white overflow-hidden shadow rounded-lg">
            <div className="p-6">
              <h3 className="text-lg font-medium text-gray-900 mb-2">
                {subject.name}
              </h3>
              <p className="text-sm text-gray-500 mb-4">
                Exam Type: {subject.exam_type}
              </p>
              <p className="text-sm text-gray-600 mb-4">
                {subject.topics.length} topics available
              </p>

              {subject.topics.length > 0 && (
                <div className="space-y-2">
                  <h4 className="text-sm font-medium text-gray-700">Topics:</h4>
                  <div className="max-h-32 overflow-y-auto">
                    {subject.topics.slice(0, 5).map((topic) => (
                      <Link
                        key={topic.id}
                        to={`/quiz/${topic.id}`}
                        className="block text-sm text-blue-600 hover:text-blue-800 hover:underline"
                      >
                        {topic.title}
                      </Link>
                    ))}
                    {subject.topics.length > 5 && (
                      <p className="text-xs text-gray-500">
                        ...and {subject.topics.length - 5} more
                      </p>
                    )}
                  </div>
                </div>
              )}

              <div className="mt-4">
                <Link
                  to={`/quiz/${subject.topics[0]?.id || ''}`}
                  className="w-full bg-blue-600 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-blue-700 text-center block disabled:opacity-50 disabled:cursor-not-allowed"
                  onClick={(e) => {
                    if (!subject.topics[0]) {
                      e.preventDefault()
                      alert('No topics available for this subject')
                    }
                  }}
                >
                  Start Studying
                </Link>
              </div>
            </div>
          </div>
        ))}
      </div>

      {subjects.length === 0 && (
        <div className="text-center py-12">
          <p className="text-gray-500">No subjects available</p>
        </div>
      )}
    </div>
  )
}