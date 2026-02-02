"""
Simple Test Script for Carmen RAG System

Run this to test the RAG system with sample queries.
"""

import sys
import io
from pathlib import Path

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from chroma_embedder import CarmenChromaDB, ThaiEnglishQueryProcessor
from response_formatter import format_response


# Troubleshooting queries - test error resolution
TROUBLESHOOTING_QUERIES = [
    # AP Troubleshooting
    ("บันทึก AP Invoice ไม่ได้", "Cannot save AP invoice"),
    ("กด Payment AP ไม่ได้", "Cannot make AP payment"),
    ("Input Tax Reconciliation ไม่ตรงกัน", "Input tax reconciliation mismatch"),

    # AR Troubleshooting
    ("บันทึก AR Invoice ไม่ได้", "Cannot save AR invoice"),
    ("รับเงิน AR ไม่ได้", "Cannot receive AR payment"),
    ("สร้างใบกำกับภาษี AR ไม่ได้", "Cannot create AR tax invoice"),

    # GL Troubleshooting
    ("บันทึก JV ไม่ได้ Dr ไม่เท่ากับ Cr", "Cannot save JV Dr not equal Cr"),
    ("แก้ไข JV ที่ Posted แล้วไม่ได้", "Cannot edit posted JV"),
    ("ปิด GL Period ไม่ได้", "Cannot close GL period"),

    # Asset Troubleshooting
    ("บันทึก Asset ไม่ได้", "Cannot save asset"),
    ("คำนวณค่าเสื่อมไม่ถูกต้อง", "Depreciation calculation incorrect"),
    ("ทำ Asset Disposal ไม่ได้", "Cannot dispose asset"),

    # Workbook Troubleshooting
    ("กดปุ่ม Refresh ไม่ได้", "Cannot press refresh button"),
    ("Carmen Add-in ไม่แสดง", "Carmen Add-in not showing"),
    ("Upload Transaction ไม่ได้", "Cannot upload transaction"),

    # Configuration Troubleshooting
    ("ลบ Account Code ไม่ได้", "Cannot delete account code"),
    ("เปลี่ยน Account Nature ไม่ได้", "Cannot change account nature"),
    ("Password ไม่ผ่าน", "Password validation failed"),
]


def test_rag():
    """Test the RAG system with sample queries."""

    # Configuration
    persist_dir = Path(__file__).parent.parent / "carmen_chroma_db"

    # Initialize database
    print("[*] Connecting to ChromaDB...")
    db = CarmenChromaDB(str(persist_dir))
    db.create_collection(reset=False)

    # Check collection info
    info = db.get_collection_info()
    print(f"\n[INFO] Collection Info:")
    print(f"   Name: {info['name']}")
    print(f"   Total Chunks: {info['count']}")

    # Sample queries in Thai and English
    test_queries = [
        ("วิธีสร้างใบแจ้งหนี้ AP", "How to create AP invoice"),
        ("วิธีคำนวณค่าเสื่อม", "How to calculate depreciation"),
        ("วิธีโพสต์ AP เข้า GL", "How to post AP to GL"),
        ("วิธีปรับสมดุลภาษีซื้อ", "How to reconcile input tax"),
        ("วิธีสร้าง Journal Voucher", "How to create journal voucher"),
    ]

    query_processor = ThaiEnglishQueryProcessor()

    print("\n" + "="*70)
    print("[TEST] RUNNING TEST QUERIES")
    print("="*70)

    for thai_query, english_query in test_queries:
        print(f"\n{'─'*70}")
        print(f"[TH] Thai:  {thai_query}")
        print(f"[EN] English: {english_query}")

        # Test Thai query
        augmented = query_processor.augment_query(thai_query)
        results = db.query(augmented, n_results=3)

        print(f"\n   Top {len(results)} Results:")
        for i, r in enumerate(results, 1):
            module = r['metadata'].get('module', 'N/A')
            doc_type = r['metadata'].get('doc_type', 'N/A')
            dist = r.get('distance', 0)

            # Truncate content
            content = r['content'][:150].replace('\n', ' ')
            if len(r['content']) > 150:
                content += "..."

            print(f"   {i}. [{module}] {doc_type} (dist: {dist:.3f})")
            print(f"      {content}")

    print("\n" + "="*70)
    print("[TEST] RUNNING TROUBLESHOOTING QUERIES")
    print("="*70)

    for thai_query, english_query in TROUBLESHOOTING_QUERIES:
        print(f"\n{'─'*70}")
        print(f"[TH] Thai:  {thai_query}")
        print(f"[EN] English: {english_query}")

        # Test Thai query
        augmented = query_processor.augment_query(thai_query)
        results = db.query(augmented, n_results=2)

        print(f"\n   Top {len(results)} Results:")
        for i, r in enumerate(results, 1):
            module = r['metadata'].get('module', 'N/A')
            doc_type = r['metadata'].get('doc_type', 'N/A')
            dist = r.get('distance', 0)

            # Truncate content
            content = r['content'][:150].replace('\n', ' ')
            if len(r['content']) > 150:
                content += "..."

            print(f"   {i}. [{module}] {doc_type} (dist: {dist:.3f})")
            print(f"      {content}")

    print("\n" + "="*70)
    print("[OK] Test completed!")
    print("="*70)


def test_troubleshooting_only():
    """Test only troubleshooting queries."""
    persist_dir = Path(__file__).parent.parent / "carmen_chroma_db"

    # Initialize database
    print("[*] Connecting to ChromaDB...")
    db = CarmenChromaDB(str(persist_dir))
    db.create_collection(reset=False)

    # Check collection info
    info = db.get_collection_info()
    print(f"\n[INFO] Collection Info:")
    print(f"   Name: {info['name']}")
    print(f"   Total Chunks: {info['count']}")

    query_processor = ThaiEnglishQueryProcessor()

    print("\n" + "="*70)
    print("[TEST] TROUBLESHOOTING QUERY TEST")
    print("="*70)

    for thai_query, english_query in TROUBLESHOOTING_QUERIES:
        print(f"\n{'─'*70}")
        print(f"[TH] {thai_query}")
        print(f"[EN] {english_query}")

        # Test Thai query
        augmented = query_processor.augment_query(thai_query)
        results = db.query(augmented, n_results=3)

        # Check if troubleshooting doc is in results
        found_troubleshooting = False
        for r in results:
            if r['metadata'].get('doc_type') == 'troubleshooting':
                found_troubleshooting = True
                break

        status = "[OK]" if found_troubleshooting else "[--]"

        print(f"\n   {status} Top {len(results)} Results:")
        for i, r in enumerate(results, 1):
            module = r['metadata'].get('module', 'N/A')
            submodule = r['metadata'].get('submodule', 'N/A')
            doc_type = r['metadata'].get('doc_type', 'N/A')
            dist = r.get('distance', 0)

            # Truncate content
            content = r['content'][:120].replace('\n', ' ')
            if len(r['content']) > 120:
                content += "..."

            print(f"   {i}. [{module}/{submodule}] {doc_type} (dist: {dist:.3f})")
            print(f"      {content}")

    print("\n" + "="*70)
    print("[OK] Troubleshooting test completed!")
    print("="*70)


def test_formatted_response():
    """Test formatted response with can/cannot indication."""
    persist_dir = Path(__file__).parent.parent / "carmen_chroma_db"

    # Initialize database
    print("[*] Connecting to ChromaDB...")
    db = CarmenChromaDB(str(persist_dir))
    db.create_collection(reset=False)

    # Check collection info
    info = db.get_collection_info()
    print(f"\n[INFO] Collection Info:")
    print(f"   Name: {info['name']}")
    print(f"   Total Chunks: {info['count']}")

    query_processor = ThaiEnglishQueryProcessor()

    # Test queries that require can/cannot answers
    test_queries = [
        "กดปุ่ม refresh ใน workbook ไม่ได้ ทำยังไง",
        "ลบ Account Code ที่ใช้งานแล้วได้ไหม",
        "แก้ไข JV ที่ Posted แล้วได้ไหม",
        "เปลี่ยน Account Nature ได้ไหม",
    ]

    print("\n" + "="*70)
    print("[TEST] FORMATTED RESPONSE TEST (Can/Cannot)")
    print("="*70)

    for query in test_queries:
        print(f"\n{'='*70}")
        print(f"[QUESTION] {query}")
        print(f"{'='*70}")

        # Augment and query - get more results for troubleshooting
        augmented = query_processor.augment_query(query)
        results = db.query(augmented, n_results=50)  # Get 50 results for troubleshooting to find solution

        # Format response
        response = format_response(query, results, language="th")
        print(response)
        print()

    print("\n" + "="*70)
    print("[OK] Formatted response test completed!")
    print("="*70)


def interactive_mode():
    """Interactive query mode."""
    persist_dir = Path(__file__).parent.parent / "carmen_chroma_db"

    print("[*] Connecting to ChromaDB...")
    db = CarmenChromaDB(str(persist_dir))
    db.create_collection(reset=False)

    query_processor = ThaiEnglishQueryProcessor()

    print("\n" + "="*70)
    print("[MODE] INTERACTIVE QUERY MODE")
    print("="*70)
    print("Commands: 'quit' to exit, 'info' for stats")
    print("-"*70)

    while True:
        try:
            user_input = input("\nQuery (Thai or English): ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break

            if user_input.lower() == 'info':
                info = db.get_collection_info()
                print(f"[INFO] Collection: {info['name']}")
                print(f"   Total chunks: {info['count']}")
                continue

            # Augment and query
            augmented = query_processor.augment_query(user_input)
            results = db.query(augmented, n_results=5)

            # Format and display response
            print(f"\n[RESULT] Found {len(results)} results for: '{user_input}'")
            print("-" * 70)

            response = format_response(user_input, results, language="th")
            print(response)
            print("-" * 70)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"[ERROR] Error: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Test Carmen RAG System")
    parser.add_argument("--interactive", "-i", action="store_true",
                       help="Run in interactive mode")
    parser.add_argument("--troubleshooting", "-t", action="store_true",
                       help="Run only troubleshooting tests")
    parser.add_argument("--format", "-f", action="store_true",
                       help="Run formatted response test (can/cannot)")
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.format:
        test_formatted_response()
    elif args.troubleshooting:
        test_troubleshooting_only()
    else:
        test_rag()
