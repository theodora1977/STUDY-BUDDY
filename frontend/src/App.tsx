import { Routes, Route } from 'react-router-dom'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import Quiz from './pages/Quiz'
import QuizResults from './pages/QuizResults'
import Progress from './pages/Progress'
import Layout from './components/Layout'
import ProtectedRoute from './components/ProtectedRoute'

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/quiz-results" element={<QuizResults />} />
      <Route path="/" element={
        <ProtectedRoute>
          <Layout />
        </ProtectedRoute>
      }>
        <Route index element={<Dashboard />} />
        <Route path="quiz/:topicId" element={<Quiz />} />
        <Route path="progress" element={<Progress />} />
      </Route>
    </Routes>
  )
}

export default App