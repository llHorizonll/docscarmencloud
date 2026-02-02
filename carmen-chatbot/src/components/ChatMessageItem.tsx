/**
 * Individual chat message component
 */
import type { ChatMessage } from '../types'
import { CanCannotBadge } from './CanCannotBadge'

interface ChatMessageItemProps {
  message: ChatMessage
}

export function ChatMessageItem({ message }: ChatMessageItemProps) {
  const isUser = message.role === 'user'

  const formatMessage = (content: string): string => {
    // Simple markdown-like formatting
    return content
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/`(.*?)`/g, '<code>$1</code>')
      .replace(/\n/g, '<br>')
  }

  const formattedContent = formatMessage(message.content)

  return (
    <div className={`carmen-chat-message ${isUser ? 'user' : 'assistant'}`}>
      <div className="carmen-message-content">
        <div
          className="carmen-message-text"
          dangerouslySetInnerHTML={{ __html: formattedContent }}
        />

        {!isUser && message.canCannot && message.canCannot !== 'unknown' && (
          <CanCannotBadge status={message.canCannot} />
        )}

        {!isUser && message.sources && message.sources.length > 0 && (
          <div className="carmen-message-sources">
            <small>ที่มา:</small>
            {message.sources.slice(0, 3).map((source, idx) => (
              source.url ? (
                <a
                  key={idx}
                  href={source.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="carmen-source-link"
                >
                  {source.module}/{source.submodule}
                </a>
              ) : (
                <span key={idx} className="carmen-source-tag">
                  {source.module}/{source.submodule}
                </span>
              )
            ))}
          </div>
        )}

        {message.timestamp && (
          <small className="carmen-message-time">
            {new Date(message.timestamp).toLocaleTimeString('th-TH', {
              hour: '2-digit',
              minute: '2-digit'
            })}
          </small>
        )}
      </div>
    </div>
  )
}
