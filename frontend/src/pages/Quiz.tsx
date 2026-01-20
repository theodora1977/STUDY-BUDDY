import { useState, useEffect } from 'react'
import { useParams, useNavigate, useLocation } from 'react-router-dom'
import axios from 'axios'

interface Question {
  id: number
  question: string
  options: { [key: string]: string }
  correct_answer: string
  explanation: string
}

interface QuizResult {
  correct: number
  total: number
  accuracy: number
}

export default function Quiz() {
  const { topicId } = useParams<{ topicId: string }>()
  const navigate = useNavigate()
  const location = useLocation()
  const [questions, setQuestions] = useState<Question[]>([])
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0)
  const [selectedAnswer, setSelectedAnswer] = useState<string>('')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [results, setResults] = useState<QuizResult>({ correct: 0, total: 0, accuracy: 0 })
  const [userAnswers, setUserAnswers] = useState<string[]>([])

  useEffect(() => {
    if (topicId) {
      fetchQuestions()
    }
  }, [topicId])

  const fetchQuestions = async () => {
    try {
      // Check if user has previous attempts for this topic (retake scenario)
      let shouldShuffle = false
      try {
        const progressResponse = await axios.get('/api/progress')
        const userProgress = progressResponse.data
        const topicProgress = userProgress.find((p: any) => p.topic_id === parseInt(topicId || '0'))
        
        // If user has attempted this quiz before, shuffle the questions
        if (topicProgress && topicProgress.attempts > 0) {
          shouldShuffle = true
        }
      } catch (progressErr) {
        // If we can't fetch progress, use the explicit shuffle param or default to false
        const searchParams = new URLSearchParams(location.search)
        shouldShuffle = searchParams.get('shuffle') === 'true'
      }
      
      const response = await axios.get(`/api/topics/${topicId}/questions`, {
        params: { shuffle: shouldShuffle }
      })
      setQuestions(response.data)
    } catch (err: any) {
      setError('Failed to load questions')
    } finally {
      setLoading(false)
    }
  }

  const handleAnswerSelect = async (answer: string) => {
    const newAnswers = [...userAnswers]
    const previousAnswer = newAnswers[currentQuestionIndex]
    const wasCorrect = previousAnswer === questions[currentQuestionIndex].correct_answer
    const isCorrect = answer === questions[currentQuestionIndex].correct_answer
    
    // Update the answer for current question
    newAnswers[currentQuestionIndex] = answer
    setSelectedAnswer(answer)
    setUserAnswers(newAnswers)

    // Adjust score if this is the first time answering or changing answer
    if (!previousAnswer) {
      // First answer to this question
      setResults(prev => ({
        correct: prev.correct + (isCorrect ? 1 : 0),
        total: prev.total + 1,
        accuracy: ((prev.correct + (isCorrect ? 1 : 0)) / (prev.total + 1)) * 100
      }))
    } else if (wasCorrect !== isCorrect) {
      // Changed from correct to wrong or wrong to correct
      setResults(prev => ({
        correct: prev.correct + (isCorrect ? 1 : -1),
        total: prev.total,
        accuracy: ((prev.correct + (isCorrect ? 1 : -1)) / prev.total) * 100
      }))
    }

    // Try to update progress, but don't block if it fails
    try {
      await axios.post('/api/progress', {
        topic_id: parseInt(topicId || '0'),
        correct: isCorrect
      })
    } catch (progressErr) {
      console.warn('Progress tracking failed, continuing anyway:', progressErr)
    }
  }

  const handleNextQuestion = async () => {
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(prev => prev + 1)
      setSelectedAnswer(userAnswers[currentQuestionIndex + 1] || '')
    } else {
      // Quiz completed - navigate to results page
      navigate('/quiz-results', {
        state: {
          questions: questions,
          userAnswers: userAnswers,
          score: results.correct,
          total: results.total,
          accuracy: results.accuracy,
          topicId: parseInt(topicId || '0')
        }
      })
    }
  }

  const handlePreviousQuestion = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(prev => prev - 1)
      setSelectedAnswer(userAnswers[currentQuestionIndex - 1] || '')
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
          onClick={() => navigate('/')}
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
        >
          Back to Dashboard
        </button>
      </div>
    )
  }

  if (questions.length === 0) {
    return (
      <div className="text-center">
        <p className="text-gray-500">No questions available for this topic</p>
        <button
          onClick={() => navigate('/')}
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
        >
          Back to Dashboard
        </button>
      </div>
    )
  }

  const currentQuestion = questions[currentQuestionIndex]
  const progress = ((currentQuestionIndex + 1) / questions.length) * 100

  return (
    <div className="max-w-2xl mx-auto">
      <div className="mb-8">
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-2xl font-bold text-gray-900">Quiz</h1>
          <button
            onClick={() => navigate('/')}
            className="text-gray-600 hover:text-gray-800"
          >
            ← Back to Dashboard
          </button>
        </div>

        <div className="w-full bg-gray-200 rounded-full h-2">
          <div
            className="bg-blue-600 h-2 rounded-full transition-all duration-300"
            style={{ width: `${progress}%` }}
          ></div>
        </div>
        <p className="text-sm text-gray-600 mt-2">
          Question {currentQuestionIndex + 1} of {questions.length}
        </p>
      </div>

      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-6">
          {currentQuestion.question}
        </h2>

        <div className="space-y-3">
          {Object.entries(currentQuestion.options).map(([key, value]) => (
            <button
              key={key}
              onClick={() => handleAnswerSelect(key)}
              className={`w-full text-left p-4 rounded-lg border transition-colors ${
                selectedAnswer === key
                  ? 'border-blue-500 bg-blue-50 text-blue-700'
                  : 'border-gray-200 hover:border-gray-300'
              }`}
            >
              <span className="font-medium mr-2">{key}.</span>
              {value}
            </button>
          ))}
        </div>

        <div className="mt-6 flex justify-between items-center">
          <button
            onClick={handlePreviousQuestion}
            disabled={currentQuestionIndex === 0}
            className={`px-4 py-2 rounded-md font-medium transition-colors ${
              currentQuestionIndex === 0
                ? 'bg-gray-200 text-gray-400 cursor-not-allowed'
                : 'bg-gray-600 text-white hover:bg-gray-700'
            }`}
          >
            ← Previous
          </button>

          <div className="flex items-center gap-4">
            <div className="text-sm text-gray-600">
              Question {currentQuestionIndex + 1} of {questions.length}
            </div>
          </div>

          <button
            onClick={handleNextQuestion}
            className={`px-4 py-2 rounded-md font-medium transition-colors ${
              currentQuestionIndex === questions.length - 1
                ? 'bg-green-600 text-white hover:bg-green-700'
                : 'bg-blue-600 text-white hover:bg-blue-700'
            }`}
          >
            {currentQuestionIndex === questions.length - 1 ? 'Finish Quiz' : 'Next →'}
          </button>
        </div>
      </div>
    </div>
  )
}