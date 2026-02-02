/**
 * Messages list component
 */
import type { ChatMessage } from '../types'
import { ChatMessageItem } from './ChatMessageItem'

interface ChatMessagesProps {
  messages: ChatMessage[]
  messagesEndRef: React.RefObject<HTMLDivElement>
  isLoading: boolean
}

export function ChatMessages({ messages, messagesEndRef, isLoading }: ChatMessagesProps) {
  return (
    <div className="carmen-chat-messages">
      {messages.map((message, idx) => (
        <ChatMessageItem key={`${message.role}-${idx}`} message={message} />
      ))}

      {isLoading && (
        <div className="carmen-chat-message assistant">
          <div className="carmen-message-content">
            <div className="carmen-typing-indicator">
              <span />
              <span />
              <span />
            </div>
          </div>
        </div>
      )}

      <div ref={messagesEndRef} />
    </div>
  )
}
