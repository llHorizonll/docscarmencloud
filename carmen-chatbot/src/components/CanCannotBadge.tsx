/**
 * Badge component for displaying Can/Cannot status
 */
import type { CanCannotStatus } from '../types'

interface CanCannotBadgeProps {
  status: CanCannotStatus
}

export function CanCannotBadge({ status }: CanCannotBadgeProps) {
  if (status === 'unknown') return null

  const getBadgeInfo = () => {
    switch (status) {
      case 'can':
        return { text: 'ได้', className: 'can-badge' }
      case 'cannot':
        return { text: 'ไม่ได้', className: 'cannot-badge' }
      case 'cannot_with_workaround':
        return { text: 'ไม่ได้ (แต่มีวิธีแก้)', className: 'workaround-badge' }
      default:
        return { text: '', className: '' }
    }
  }

  const { text, className } = getBadgeInfo()

  return (
    <span className={`carmen-can-cannot-badge ${className}`}>
      {text}
    </span>
  )
}
