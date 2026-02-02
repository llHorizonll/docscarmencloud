/**
 * Main chat widget component
 */
import { useEffect, useState } from 'react'
import { useChatbot } from '../hooks/useChatbot'
import { useRagApi } from '../hooks/useRagApi'
import { ToggleButton } from './ToggleButton'
import { ChatHeader } from './ChatHeader'
import { ChatMessages } from './ChatMessages'
import { ChatInput } from './ChatInput'

interface ChatWidgetProps {
  apiUrl?: string
}

export function ChatWidget({ apiUrl }: ChatWidgetProps) {
  const {
    isOpen,
    isMinimized,
    messages,
    messagesEndRef,
    assistantMessageCount,
    toggleChat,
    minimizeChat,
    clearChat,
    addMessage,
    setIsOpen
  } = useChatbot()

  const { query, checkHealth, isLoading } = useRagApi(apiUrl)
  const [isHealthy, setIsHealthy] = useState(false)

  // Check API health on mount
  useEffect(() => {
    checkHealth().then(setIsHealthy)
  }, [checkHealth])

  // Handle sending messages
  const handleSend = async (messageText: string) => {
    // Add user message
    addMessage({
      role: 'user',
      content: messageText
    })

    // Query API
    await query(
      messageText,
      (response) => {
        addMessage({
          role: 'assistant',
          content: response.answer,
          canCannot: response.can_cannot,
          sources: response.sources
        })
      },
      (error) => {
        addMessage({
          role: 'assistant',
          content: `ขออภัยครับ เกิดข้อผิดพลาดในการเชื่อมต่อ: ${error}\n\nSorry, an error occurred: ${error}`
        })
      }
    )
  }

  // Expose close function globally
  useEffect(() => {
    ;(window as any).CarmenChatbot = {
      ...(window as any).CarmenChatbot,
      close: () => setIsOpen(false)
    }
  }, [setIsOpen])

  return (
    <div className="carmen-chatbot-container">
      <ToggleButton
        isOpen={isOpen}
        onClick={toggleChat}
        messageCount={assistantMessageCount}
      />

      {isOpen && (
        <div className={`carmen-chat-window ${isMinimized ? 'minimized' : ''}`}>
          <ChatHeader
            isMinimized={isMinimized}
            onMinimize={minimizeChat}
            onClear={clearChat}
            isHealthy={isHealthy}
          />

          {!isMinimized && (
            <>
              <ChatMessages
                messages={messages}
                messagesEndRef={messagesEndRef}
                isLoading={isLoading}
              />
              <ChatInput
                disabled={isLoading}
                onSend={handleSend}
                placeholder="พิมพ์คำถาม..."
              />
            </>
          )}
        </div>
      )}
    </div>
  )
}
