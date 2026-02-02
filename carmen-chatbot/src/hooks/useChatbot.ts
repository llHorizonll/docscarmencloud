/**
 * Hook for chatbot state management
 */
import { useState, useCallback, useEffect, useRef } from 'react'
import { flushSync } from 'react-dom'
import { useLocalStorage, STORAGE_KEY } from './useLocalStorage'
import type { ChatMessage } from '../types'

const WELCOME_MESSAGE: ChatMessage = {
  role: 'assistant',
  content: 'สวัสดีครับ! ผมคือ AI ผู้ช่วยสำหรับเอกสาร Carmen Cloud มีคำถามอะไรไหมครับ?\n\nHello! I\'m the AI assistant for Carmen Cloud documentation. How can I help you?',
  timestamp: Date.now()
}

export function useChatbot() {
  const [isOpen, setIsOpen] = useState(false)
  const [isMinimized, setIsMinimized] = useState(false)
  const [messages, setMessages, clearMessages] = useLocalStorage<ChatMessage[]>(
    STORAGE_KEY,
    [WELCOME_MESSAGE]
  )
  const messagesEndRef = useRef<HTMLDivElement>(null)

  // Track latest messages to avoid stale closures
  const messagesRef = useRef<ChatMessage[]>(messages)
  messagesRef.current = messages

  // Track if we've loaded from localStorage to prevent overwrites
  const isInitializedRef = useRef(false)

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    if (isInitializedRef.current) {
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
    }
  }, [messages])

  const toggleChat = useCallback(() => {
    setIsOpen((prev) => {
      const newValue = !prev
      // Reset minimized when opening
      if (newValue) {
        setIsMinimized(false)
      }
      return newValue
    })
  }, [])

  const minimizeChat = useCallback(() => {
    setIsMinimized((prev) => !prev)
  }, [])

  const clearChat = useCallback(() => {
    clearMessages()
  }, [clearMessages])

  const addMessage = useCallback((message: Omit<ChatMessage, 'timestamp'>) => {
    console.log('[useChatbot] Adding message:', message)
    // Use latest messages from ref to avoid stale state
    const latestMessages = messagesRef.current
    const newMessage = { ...message, timestamp: Date.now() }
    const newMessages = [...latestMessages, newMessage]

    console.log('[useChatbot] New messages array:', newMessages)
    console.log('[useChatbot] User messages count:', newMessages.filter(m => m.role === 'user').length)
    console.log('[useChatbot] Assistant messages count:', newMessages.filter(m => m.role === 'assistant').length)

    // Use flushSync to force immediate update
    flushSync(() => {
      setMessages(newMessages)
    })

    // Update ref immediately
    messagesRef.current = newMessages
    isInitializedRef.current = true
  }, [])

  // Mark as initialized on mount after loading from localStorage
  useEffect(() => {
    isInitializedRef.current = true
  }, [])

  const assistantMessageCount = messages.filter((m) => m.role === 'assistant').length

  return {
    isOpen,
    isMinimized,
    messages,
    messagesEndRef,
    assistantMessageCount,
    toggleChat,
    minimizeChat,
    clearChat,
    addMessage,
    setIsOpen,
    setIsMinimized
  }
}
