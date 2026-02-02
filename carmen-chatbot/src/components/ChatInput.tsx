/**
 * Chat input component
 */
import { useState, useEffect, useRef } from 'react'

interface ChatInputProps {
  disabled?: boolean
  placeholder?: string
  onSend: (message: string) => void
}

export function ChatInput({
  disabled = false,
  placeholder = 'พิมพ์คำถาม...',
  onSend
}: ChatInputProps) {
  const [input, setInput] = useState('')
  const textareaRef = useRef<HTMLTextAreaElement>(null)

  useEffect(() => {
    // Auto-resize textarea
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto'
      const newHeight = Math.min(textareaRef.current.scrollHeight, 120)
      textareaRef.current.style.height = `${newHeight}px`
    }
  }, [input])

  const handleSend = () => {
    const message = input.trim()
    if (message && !disabled) {
      onSend(message)
      setInput('')
      if (textareaRef.current) {
        textareaRef.current.style.height = 'auto'
      }
    }
  }

  const handleKeydown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <div className="carmen-chat-input-container">
      <textarea
        ref={textareaRef}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={handleKeydown}
        disabled={disabled}
        placeholder={placeholder}
        className="carmen-chat-textarea"
        rows={1}
      />
      <button
        disabled={disabled || !input.trim()}
        className="carmen-send-button"
        onClick={handleSend}
        type="button"
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z" />
        </svg>
      </button>
    </div>
  )
}
