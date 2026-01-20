import { useLocation, useNavigate } from 'react-router-dom'

interface Question {
  id: number
  question: string
  options: { [key: string]: string }
  correct_answer: string
  explanation: string
}

interface UserAnswer {
  question: Question
  userAnswer: string
  isCorrect: boolean
}

export default function QuizResults() {
  const location = useLocation()
  const navigate = useNavigate()
  const state = location.state as {
    questions: Question[]
    userAnswers: string[]
    score: number
    total: number
    accuracy: number
    topicId?: number
  }

  if (!state || !state.questions) {
    return (
      <div className="text-center py-8">
        <p className="text-gray-500">No quiz results found</p>
        <button
          onClick={() => navigate('/')}
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
        >
          Back to Dashboard
        </button>
      </div>
    )
  }

  const { questions, userAnswers, score, total, accuracy, topicId } = state

  const handleRetakeQuiz = () => {
    if (topicId) {
      navigate(`/quiz/${topicId}?shuffle=true`)
    }
  }

  const userAnswersData: UserAnswer[] = questions.map((question, index) => ({
    question,
    userAnswer: userAnswers[index] || '',
    isCorrect: userAnswers[index] === question.correct_answer
  }))

  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-8">
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-3xl font-bold text-gray-900">Quiz Results</h1>
          <button
            onClick={() => navigate('/')}
            className="text-gray-600 hover:text-gray-800"
          >
            ← Back to Dashboard
          </button>
        </div>

        {/* Score Summary */}
        <div className="bg-gradient-to-r from-blue-600 to-blue-800 text-white rounded-lg p-8 mb-8">
          <div className="grid grid-cols-3 gap-6">
            <div className="text-center">
              <p className="text-4xl font-bold">{score}</p>
              <p className="text-blue-100">Correct Answers</p>
            </div>
            <div className="text-center">
              <p className="text-4xl font-bold">{total}</p>
              <p className="text-blue-100">Total Questions</p>
            </div>
            <div className="text-center">
              <p className="text-4xl font-bold">{accuracy.toFixed(1)}%</p>
              <p className="text-blue-100">Accuracy</p>
            </div>
          </div>
        </div>

        {/* Performance Feedback */}
        <div className={`p-4 rounded-lg mb-8 ${
          accuracy >= 80
            ? 'bg-green-50 border border-green-200'
            : accuracy >= 60
            ? 'bg-yellow-50 border border-yellow-200'
            : 'bg-red-50 border border-red-200'
        }`}>
          <p className={`font-semibold ${
            accuracy >= 80
              ? 'text-green-800'
              : accuracy >= 60
              ? 'text-yellow-800'
              : 'text-red-800'
          }`}>
            {accuracy >= 80
              ? '🎉 Excellent! You performed very well!'
              : accuracy >= 60
              ? '👍 Good effort! Keep practicing to improve.'
              : '💪 Keep working on these topics. Review the explanations below.'}
          </p>
        </div>
      </div>

      {/* Detailed Review */}
      <div className="space-y-6">
        <h2 className="text-2xl font-bold text-gray-900">Detailed Review</h2>

        {userAnswersData.map((item, index) => (
          <div
            key={index}
            className={`p-6 rounded-lg border-l-4 ${
              item.isCorrect
                ? 'bg-green-50 border-green-500'
                : 'bg-red-50 border-red-500'
            }`}
          >
            {/* Question Number and Status */}
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold text-gray-900">
                Question {index + 1}
              </h3>
              <span className={`px-3 py-1 rounded-full text-sm font-medium ${
                item.isCorrect
                  ? 'bg-green-200 text-green-800'
                  : 'bg-red-200 text-red-800'
              }`}>
                {item.isCorrect ? '✓ Correct' : '✗ Incorrect'}
              </span>
            </div>

            {/* Question Text */}
            <p className="text-gray-800 font-medium mb-4">
              {item.question.question}
            </p>

            {/* Options */}
            <div className="space-y-2 mb-4">
              {Object.entries(item.question.options).map(([key, value]) => {
                const isUserAnswer = key === item.userAnswer
                const isCorrectAnswer = key === item.question.correct_answer

                return (
                  <div
                    key={key}
                    className={`p-3 rounded ${
                      isCorrectAnswer
                        ? 'bg-green-100 border-l-4 border-green-500'
                        : isUserAnswer && !item.isCorrect
                        ? 'bg-red-100 border-l-4 border-red-500'
                        : 'bg-gray-100'
                    }`}
                  >
                    <span className="font-medium text-gray-900">{key}.</span>
                    <span className="ml-2 text-gray-800">{value}</span>
                    {isCorrectAnswer && (
                      <span className="ml-2 text-green-700 font-semibold">✓ Correct Answer</span>
                    )}
                    {isUserAnswer && !item.isCorrect && (
                      <span className="ml-2 text-red-700 font-semibold">✗ Your Answer</span>
                    )}
                  </div>
                )
              })}
            </div>

            {/* Explanation */}
            <div className="bg-white p-4 rounded border border-gray-200">
              <p className="text-sm font-semibold text-gray-900 mb-2">Explanation:</p>
              <p className="text-gray-700">{item.question.explanation}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Action Buttons */}
      <div className="mt-8 flex justify-center gap-4">
        {topicId && (
          <button
            onClick={handleRetakeQuiz}
            className="bg-green-600 text-white px-6 py-2 rounded-md hover:bg-green-700"
          >
            Take Quiz Again (Shuffled)
          </button>
        )}
        <button
          onClick={() => navigate('/progress')}
          className="bg-blue-600 text-white px-6 py-2 rounded-md hover:bg-blue-700"
        >
          View Progress
        </button>
        <button
          onClick={() => navigate('/')}
          className="bg-gray-600 text-white px-6 py-2 rounded-md hover:bg-gray-700"
        >
          Back to Dashboard
        </button>
      </div>
    </div>
  )
}
