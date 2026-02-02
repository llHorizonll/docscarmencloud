"""
Response Formatter for Carmen RAG System

Formats retrieved chunks into user-friendly responses with:
1. Clear "Can do" / "Cannot do" indication
2. Structured answers
3. Follow-up questions when info is insufficient
"""

import re
from typing import List, Dict, Any, Optional


class CarmenResponseFormatter:
    """Format RAG results into structured responses."""

    # Keywords that indicate capability/possibility
    CANNOT_DO_KEYWORDS_TH = [
        "ไม่ได้", "ไม่สามารถ", "ไม่เป็นไปได้", "ทำไม่ได้",
        "ใช้ไม่ได้", "ไม่สามารถทำ", "กระทำไม่ได้", "ดำเนินการไม่ได้",
        "ห้าม", "ไม่อนุญาต", "ไม่รองรับ"
    ]

    CAN_DO_KEYWORDS_TH = [
        "ได้", "สามารถ", "เป็นไปได้", "ทำได้", "ใช้ได้",
        "สามารถทำ", "กระทำได้", "ดำเนินการได้"
    ]

    # Actions that typically have "cannot" answers
    CANNOT_ACTIONS = [
        "ลบ", "แก้ไข", "เปลี่ยน", "delete", "edit", "change"
    ]

    @classmethod
    def format_response(
        cls,
        query: str,
        results: List[Dict[str, Any]],
        language: str = "th"
    ) -> str:
        """
        Format RAG results into a structured response.
        """
        if not results:
            return cls._ask_for_more_info(query, language)

        # Check if this is a troubleshooting query
        is_troubleshooting = cls._is_troubleshooting_query(query)

        if is_troubleshooting:
            # For troubleshooting, use more results with looser filter
            relevant_results = [r for r in results if r.get('distance', 1) < 1.2][:50]
            if not relevant_results:
                relevant_results = results[:50]
            return cls._format_troubleshooting_response(query, relevant_results, language)
        else:
            # For normal queries, use stricter filter
            relevant_results = [r for r in results if r.get('distance', 1) < 0.75]
            if not relevant_results:
                relevant_results = results[:2]
            return cls._format_simple_response(query, relevant_results, language)

    @classmethod
    def _is_troubleshooting_query(cls, query: str) -> bool:
        """Check if query is about a problem/troubleshooting."""
        keywords = [
            "ไม่ได้", "ไม่สามารถ", "error", "ผิดพลาด",
            "ปัญหา", "แก้ไข", "fix", "troubleshooting",
            "cannot", "can't", "not working",
            "ได้ไหม", "ไหม", "ทำได้ไหม", "ทำยังไง", "วิธี"  # Also detect questions
        ]
        return any(kw in query.lower() for kw in keywords)

    @classmethod
    def _is_cannot_question(cls, query: str) -> bool:
        """
        Check if the question is asking if something CAN be done,
        but the answer is typically "cannot" (with a workaround).

        Examples:
        - "ลบ Account Code ได้ไหม" -> Cannot (but can set to Inactive)
        - "แก้ไข JV Posted ได้ไหม" -> Cannot
        - "เปลี่ยน Account Nature ได้ไหม" -> Cannot
        """
        query_lower = query.lower()

        # Check if it's a "ได้ไหม" question (can you? / is it possible?)
        is_question = any(kw in query for kw in ["ได้ไหม", "ไหม", "ทำได้ไหม", "ได้บ้าง"])

        # Check if it's about actions that typically have "cannot" answers
        has_cannot_action = any(action in query_lower for action in cls.CANNOT_ACTIONS)

        # Specific subjects that have restrictions
        restricted_subjects = [
            "account code", "account nature", "jv", "journal",
            "posted", "โพสต์แล้ว", "inactiv", "ยังใช้"
        ]
        has_restricted_subject = any(subject in query_lower for subject in restricted_subjects)

        return is_question and (has_cannot_action or has_restricted_subject)

    @classmethod
    def _determine_can_cannot_answer(cls, query: str, content: str, has_solution_marker: bool = False) -> str:
        """
        Determine if the answer is "ได้" (can) or "ไม่ได้" (cannot).
        Returns the answer header line.
        """
        query_lower = query.lower()

        # Check if this is a "cannot" question
        if cls._is_cannot_question(query):
            # Look for explicit solution markers that indicate a workaround
            has_workaround = (
                "วิธีแก้ไขที่ถูกต้อง" in content or
                ("inactive" in content.lower() and "status" in content.lower()) or
                ("ไม่สามารถ" in content and "แต่" in content) or
                ("แต่สามารถ" in content) or  # "แต่สามารถทำ Reversal ได้"
                ("reversal" in content.lower()) or  # JV reversal workaround
                has_solution_marker  # If we found the marker in raw results
            )

            if has_workaround:
                return "**ไม่ได้** (แต่มีวิธีแก้ไข)"
            else:
                return "**ไม่ได้**"

        # Check if query contains "ไม่ได้" (problem statement)
        if "ไม่ได้" in query or "cannot" in query_lower:
            has_solution = any(kw in content for kw in cls.CAN_DO_KEYWORDS_TH)
            if has_solution or "วิธีแก้" in content or "Solutions" in content or "สาเหตุ" in content:
                return "**ได้** (มีวิธีแก้ไข)"
            else:
                return "**ไม่ได้**"

        # Default: show as "here's the solution"
        return "**เข้าใจปัญหาแล้ว นี่คือวิธีแก้ไข:**"

    @classmethod
    def _extract_solution_from_all_results(cls, results: List[Dict[str, Any]], query: str) -> str:
        """
        Extract the best solution content from all results.
        Prioritizes solution markers and relevant sections.
        """
        query_lower = query.lower()

        # Extract query keywords for relevance scoring
        query_keywords = []
        if 'refresh' in query_lower or 'รีเฟรช' in query_lower:
            query_keywords.extend(['refresh', 'รีเฟรช', 'unblock', 'add-in'])
        if 'workbook' in query_lower:
            query_keywords.extend(['workbook', 'excel'])
        if 'account code' in query_lower:
            query_keywords.extend(['account code', 'acc.', 'inactive'])
        if 'account nature' in query_lower:
            query_keywords.extend(['account nature', 'acc.', 'หมวด'])
        if 'jv' in query_lower or 'journal' in query_lower or 'posted' in query_lower:
            query_keywords.extend(['jv', 'journal', 'posted', 'reversal', 'โพสต์'])

        # Find all results with solution markers and score them
        candidates = []

        for result in results:
            content = result.get('content', '')
            content_lower = content.lower()

            # Check for solution markers
            has_thai_marker = 'วิธีแก้ไขที่ถูกต้อง' in content
            has_solutions_marker = 'Solutions:' in content or 'วิธีแก้:' in content

            if has_thai_marker or has_solutions_marker:
                # Score based on query keyword matches
                score = sum(1 for kw in query_keywords if kw in content_lower)
                candidates.append((score, result, has_thai_marker, has_solutions_marker))

        # Sort by score descending
        candidates.sort(key=lambda x: x[0], reverse=True)

        # Use the best scoring candidate
        for score, result, has_thai_marker, has_solutions_marker in candidates:
            if score <= 0:
                continue  # Skip candidates with no relevant keywords

            content = result.get('content', '')

            # Extract content after the marker
            if has_thai_marker:
                marker = 'วิธีแก้ไขที่ถูกต้อง'
            else:
                marker = 'Solutions:'
                if 'วิธีแก้:' in content:
                    marker = 'วิธีแก้:'

            parts = content.split(marker)
            if len(parts) > 1:
                solution_part = parts[1].split('---')[0]
                # Clean and return
                lines = []
                for line in solution_part.split('\n')[:15]:
                    line = line.strip()
                    if line and not line.startswith('```') and not line.startswith('##'):
                        lines.append(line)
                if lines:
                    return '\n'.join(lines)

        # Third, use the section matching pattern
        best_content = results[0].get('content', '')
        for result in results[:5]:
            content = result.get('content', '')
            if len(content) > len(best_content):
                best_content = content

        matching_section = cls._find_matching_section(query, best_content)
        if matching_section:
            return matching_section

        # Finally, return cleaned first result
        return cls._clean_first_result(results[0])

    @classmethod
    def _clean_first_result(cls, result: Dict[str, Any]) -> str:
        """Clean and format the first result for display."""
        content = result.get('content', '')
        content = re.sub(r'\[EN: [^\]]+\]\s*', '', content)
        content = re.sub(r'\*\*', '', content)

        lines = []
        for line in content.split('\n')[:20]:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('```'):
                lines.append(line)

        return '\n'.join(lines)

    @classmethod
    def _format_troubleshooting_response(
        cls,
        query: str,
        results: List[Dict[str, Any]],
        language: str
    ) -> str:
        """Format troubleshooting response."""
        lines = []

        metadata = results[0].get('metadata', {})

        # Extract the best solution content FIRST
        solution_content = cls._extract_solution_from_all_results(results, query)

        # Also check if any result has the solution marker (for answer header)
        has_solution_marker = any('วิธีแก้ไขที่ถูกต้อง' in r.get('content', '') for r in results)
        has_solutions_marker = any('Solutions:' in r.get('content', '') or 'วิธีแก้:' in r.get('content', '') for r in results)

        # Determine the answer header based on the solution content
        # Also consider if we found solution markers in the raw results
        answer_header = cls._determine_can_cannot_answer(query, solution_content, has_solution_marker or has_solutions_marker)
        lines.append(answer_header)
        lines.append("")

        # Add the solution content
        if solution_content:
            for line in solution_content.split('\n'):
                if line.strip():
                    lines.append(line.strip())

        # Checklist
        checklist = cls._extract_checklist(results)
        if checklist:
            lines.append("")
            lines.append("**Checklist ตรวจสอบ:**")
            lines.append(checklist)

        # Source
        module = metadata.get('module', 'N/A')
        submodule = metadata.get('submodule', 'N/A')
        lines.append("")
        lines.append(f"ที่มา: {module}/{submodule}")

        return "\n".join(lines)

    @classmethod
    def _extract_checklist(cls, results: List[Dict[str, Any]]) -> Optional[str]:
        """Extract checklist items from results."""
        for result in results:
            content = result.get('content', '')
            if '[ ]' in content or '[x]' in content:
                items = []
                for line in content.split('\n'):
                    if '[ ]' in line or '[x]' in line:
                        items.append(f"  {line.strip()}")
                if items:
                    return '\n'.join(items[:5])
        return None

    @classmethod
    def _format_simple_response(
        cls,
        query: str,
        results: List[Dict[str, Any]],
        language: str
    ) -> str:
        """Format simple response."""
        lines = []

        for i, result in enumerate(results[:2], 1):
            content = result.get('content', '')
            metadata = result.get('metadata', {})

            content = cls._clean_content(content)

            lines.append(f"**{i}.**")
            for line in content.split('\n')[:8]:
                line = line.strip()
                if line and not line.startswith('#'):
                    lines.append(f"   {line}")

            module = metadata.get('module', 'N/A')
            lines.append(f"   ที่มา: {module}")
            lines.append("")

        return "\n".join(lines)

    @classmethod
    def _find_matching_section(cls, query: str, content: str) -> Optional[str]:
        """Find section matching the query."""
        query_lower = query.lower()

        # Map query keywords to section patterns
        patterns = [
            # (keywords, pattern)
            (['refresh', 'รีเฟรช'], r'##.*?(?:refresh|ปุ่ม).*?\n([\s\S]*?)(?=##|\Z)'),
            (['delete', 'ลบ', 'account code', 'รหัสบัญชี'], r'##.*?ลบข้อมูล configuration.*?\n([\s\S]*?)(?=##|\Z)|##\s*\d+\.\s*ลบ.*?\n([\s\S]*?)(?=##|\Z)'),
            (['account nature', 'acc. nature', 'หมวดบัญชี'], r'##.*?account nature.*?\n([\s\S]*?)(?=##|\Z)|##.*?เปลี่ยน account nature.*?\n([\s\S]*?)(?=##|\Z)'),
            (['password', 'รหัสผ่าน'], r'##.*?password.*?\n([\s\S]*?)(?=##|\Z)'),
            (['jv', 'journal', 'posted', 'โพสต์'], r'##.*?(?:journal|posted|jv).*?\n([\s\S]*?)(?=##|\Z)'),
            (['asset', 'ทรัพย์สิน', 'สินทรัพย์'], r'##.*?asset.*?\n([\s\S]*?)(?=##|\Z)|##.*?ทรัพย์สิน.*?\n([\s\S]*?)(?=##|\Z)'),
        ]

        for keywords, pattern in patterns:
            if any(kw in query_lower for kw in keywords):
                match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
                if match:
                    # Get the matched group (handle multiple groups)
                    section_content = None
                    for i in range(1, len(match.groups()) + 1):
                        if match.group(i):
                            section_content = match.group(i)
                            break

                    if not section_content:
                        continue

                    lines = []
                    for line in section_content.split('\n')[:25]:
                        line = line.strip()
                        if line and not line.startswith('#') and not line.startswith('```'):
                            # Clean up bullet points
                            if line.startswith(('- ', '* ')):
                                line = '- ' + line[2:]
                            lines.append(line)

                    if lines:
                        return '\n'.join(lines)

        return None

    @classmethod
    def _clean_content(cls, content: str) -> str:
        """Clean content for display."""
        # Remove [EN: ...] prefix
        content = re.sub(r'\[EN: [^\]]+\]\s*', '', content)
        # Remove excessive formatting
        content = re.sub(r'\*\*', '', content)
        return content.strip()

    @classmethod
    def _ask_for_more_info(cls, query: str, language: str) -> str:
        """Generate follow-up question when info is insufficient."""
        if language == "th":
            return """**ขออภัย ข้อมูลไม่เพียงพอ**

ต้องการขอข้อมูลเพิ่มเติมเพื่อให้ตอบคำถามได้ตรงจุด:
- คุณกำลังใช้งาน Module ไหน? (AP, AR, GL, Asset, Workbook)
- ตอนนี้อยู่ขั้นตอนไหนของการทำงาน?
- มีข้อความ Error แสดงขึ้นมาหรือไม่? ถ้ามาคืออะไร?

กรุณาให้รายละเอียดเพิ่มเติม"""
        else:
            return """**Sorry, insufficient information**

Please provide more details:
- Which Module are you using? (AP, AR, GL, Asset, Workbook)
- What step are you currently on?
- Is there an Error message? If yes, what does it say?

Please provide more details."""


def format_response(query: str, results: List[Dict[str, Any]], language: str = "th") -> str:
    """
    Convenience function to format RAG response.

    Args:
        query: User's question
        results: Retrieved chunks from RAG
        language: Response language (th/en)

    Returns:
        Formatted response string
    """
    formatter = CarmenResponseFormatter()
    return formatter.format_response(query, results, language)
