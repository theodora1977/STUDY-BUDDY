import { useState, useEffect } from 'react'
import axios from 'axios'

interface Progress {
  id: number
  topic_id: number
  attempts: number
  correct: number
  accuracy: number
  last_updated: string
}

interface Topic {
  id: number
  title: string
  subject_id: number
}

interface Subject {
  id: number
  name: string
  exam_type: string
}

interface ProgressWithDetails extends Progress {
  topic?: Topic
  subject?: Subject
}

export default function Progress() {
  const [progress, setProgress] = useState<ProgressWithDetails[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchProgress()
  }, [])

  const fetchProgress = async () => {
    try {
      const [progressResponse, subjectsResponse] = await Promise.all([
        axios.get('/api/progress'),
        axios.get('/api/subjects')
      ])

      const progressData = progressResponse.data
      const subjectsData = subjectsResponse.data

      // Create a map of subjects and topics for lookup
      const subjectsMap = new Map<number, Subject>()
      const topicsMap = new Map<number, Topic>()

      for (const subject of subjectsData) {
        subjectsMap.set(subject.id, subject)
        try {
          const topicsResponse = await axios.get(`/api/subjects/${subject.id}/topics`)
          for (const topic of topicsResponse.data) {
            topicsMap.set(topic.id, { ...topic, subject_id: subject.id })
          }
        } catch (err) {
          // Ignore errors for individual topic fetches
        }
      }

      // Combine progress with topic and subject data
      const progressWithDetails = progressData.map((p: Progress) => ({
        ...p,
        topic: topicsMap.get(p.topic_id),
        subject: topicsMap.get(p.topic_id) ? subjectsMap.get(topicsMap.get(p.topic_id)!.subject_id) : undefined
      }))

      setProgress(progressWithDetails)
    } catch (err: any) {
      setError('Failed to load progress')
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
          onClick={fetchProgress}
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
        >
          Retry
        </button>
      </div>
    )
  }

  const totalAttempts = progress.reduce((sum, p) => sum + p.attempts, 0)
  const totalCorrect = progress.reduce((sum, p) => sum + p.correct, 0)
  const overallAccuracy = totalAttempts > 0 ? (totalCorrect / totalAttempts) * 100 : 0

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Your Progress</h1>
        <p className="mt-2 text-gray-600">Track your learning journey</p>
      </div>

      {/* Overall Statistics */}
      <div className="bg-white shadow rounded-lg p-6 mb-8">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">Overall Statistics</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="text-center">
            <div className="text-2xl font-bold text-blue-600">{totalAttempts}</div>
            <div className="text-sm text-gray-600">Total Attempts</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-green-600">{totalCorrect}</div>
            <div className="text-sm text-gray-600">Correct Answers</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-purple-600">{overallAccuracy.toFixed(1)}%</div>
            <div className="text-sm text-gray-600">Overall Accuracy</div>
          </div>
        </div>
      </div>

      {/* Progress by Topic */}
      <div className="bg-white shadow rounded-lg">
        <div className="px-6 py-4 border-b border-gray-200">
          <h2 className="text-xl font-semibold text-gray-900">Progress by Topic</h2>
        </div>
        <div className="divide-y divide-gray-200">
          {progress.length === 0 ? (
            <div className="p-6 text-center text-gray-500">
              No progress data available. Start taking quizzes to see your progress!
            </div>
          ) : (
            progress.map((item) => (
              <div key={item.id} className="p-6">
                <div className="flex justify-between items-start mb-2">
                  <div>
                    <h3 className="text-lg font-medium text-gray-900">
                      {item.topic?.title || `Topic ${item.topic_id}`}
                    </h3>
                    {item.subject && (
                      <p className="text-sm text-gray-600">
                        {item.subject.name} • {item.subject.exam_type}
                      </p>
                    )}
                  </div>
                  <div className="text-right">
                    <div className="text-lg font-semibold text-gray-900">
                      {item.accuracy.toFixed(1)}%
                    </div>
                    <div className="text-sm text-gray-600">
                      {item.correct}/{item.attempts} correct
                    </div>
                  </div>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div
                    className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                    style={{ width: `${item.accuracy}%` }}
                  ></div>
                </div>
                <div className="mt-2 text-xs text-gray-500">
                  Last updated: {new Date(item.last_updated).toLocaleDateString()}
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  )
}