# AGENT.md - Carmen System Knowledge Base for AI Agents

## Purpose

This document serves as a comprehensive knowledge base for AI agents to autonomously learn and understand the Carmen Cloud accounting system. It provides context, terminology, and cross-references to enable effective assistance with RAG implementation and user support.

---

## System Overview

### What is Carmen Cloud?

**Carmen Cloud** is a comprehensive cloud-based accounting ERP system designed for businesses in Southeast Asia (primarily Thailand and Philippines). It provides integrated modules for managing financial operations, inventory, and assets.

### Core Product Lines

1. **Carmen Cloud** - Primary cloud accounting system
2. **BlueLedgers** - Inventory and procurement management system
3. **CADENA** - Additional module (minimal documentation)

---

## Module Structure

### Carmen Cloud Modules

| Module | Thai Name | Purpose | Key Functions |
|--------|-----------|---------|---------------|
| **AP** | Account Payable | บันทึกบัญชีเจ้าหนี้การค้า | Invoice, Payment, Vendor, Tax Reconciliation, Deposit |
| **AR** | Account Receivable | บันทึกบัญชีลูกหนี้การค้า | Invoice, Receipt, Contract, Debit Note, Credit Note |
| **GL** | General Ledger |สมุดบัญชีรายวัน/บัญชีแยกประเภท | Journal Voucher, Budget, Posting from other modules |
| **Asset** | Fixed Assets | บันทึกทะเบียนสินทรัพย์ | Asset Register, Depreciation, Disposal, Transfer |
| **Configuration** | System Config | การตั้งค่าระบบ | Chart of Accounts, Currency, Users, Departments |
| **Workbook** | Excel Integration | การเชื่อมต่อ Excel | Function mapping, Data import/export |

### BlueLedgers Modules

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| **Material** | Inventory Management | Stock In, Stock Out, Adjustment, Closing Balance |
| **Procurement** | Purchase Management | Purchase Order, Goods Receiving, Supplier Management |
| **Portions** | Recipe Management | Recipe creation, Cost calculation |
| **Options** | System Settings | Configuration options |

---

## Accounting Terminology (Thai-English)

### Core Accounting Terms

| Thai | English | Definition |
|------|---------|------------|
| สมุดบัญชีรายวัน | Journal Voucher (JV) | Daily book of accounting entries |
| บัญชีแยกประเภท | General Ledger (GL) | Main accounting ledger |
| บันทึกบัญชี | Post/Record | To record accounting entries |
| บัญชีเจ้าหนี้ | Account Payable (AP) | Money owed to suppliers |
| บัญชีลูกหนี้ | Account Receivable (AR) | Money owed by customers |
| ใบแจ้งหนี้ | Invoice | Bill for goods/services |
| ใบเสร็จรับเงิน | Receipt | Proof of payment |
| ใบกำกับภาษี | Tax Invoice | Official tax document |
| ภาษีมูลค่าเพิ่ม | VAT (Value Added Tax) | 7% tax in Thailand |
| ภาษีหัก ณ ที่จ่าย | Withholding Tax (WHT) | Tax deducted at source |
| ค่าเสื่อมราคา | Depreciation | Asset value reduction over time |
| ค่าเสื่อมราคาสะสม | Accumulated Depreciation | Total depreciation to date |
| มูลค่าซาก | Salvage Value | Residual value at end of life |
| ผังบัญชี | Chart of Accounts (COA) | List of account codes |
| งบดุล | Balance Sheet | Financial position statement |
| งบกำไรขาดทุน | Income Statement | Profit/Loss statement |
| วงเงินอนุมัติ | Credit Limit | Maximum credit allowed |

### Tax-Specific Terms (Thailand)

| Thai | English | Description |
|------|---------|-------------|
| ภ.ง.ด. 3 | PND 3 | Monthly VAT return form |
| ภ.ง.ด. 53 | PND 53 | Withholding tax return form |
| ภาษีซื้อ | Input Tax | VAT paid on purchases |
| ภาษีขาย | Output Tax | VAT collected on sales |
| ใบเบิกค่าใช้จ่าย | Expense Report | Reimbursement request |
| RDPrep | Revenue Department Prep | Software for tax preparation |

### Tax-Specific Terms (Philippines)

| Thai | English | Description |
|------|---------|-------------|
| BIR Form | Bureau of Internal Revenue Form | Philippine tax forms |
| Input Tax Reconciliation | การปรับสมดุลภาษีซื้อ | Matching input tax claims |
| 2306 | BIR Form 2306 | Withholding tax final |
| 2307 | BIR Form 2307 | Creditable tax withheld |

### System-Specific Terms

| Thai | English | Description |
|------|---------|-------------|
| โพสต์ | Post | Transfer data to GL |
| ปิดงวดบัญชี | Close Period | Lock accounting period |
| ปิดประจำปี | Year End Close | Annual closing process |
| รหัสบัญชี | Account Code | Chart of account code |
| รหัสแผนก | Department Code | Organizational unit code |
| สกุลเงิน | Currency | Currency code (THB, USD, etc.) |
| อัตราแลกเปลี่ยน | Exchange Rate | Currency conversion rate |
| เครดิตเทอม | Credit Term | Payment period (days) |
| วันครบกำหนดชำระ | Due Date | Payment deadline |

---

## Document Naming Conventions

### Carmen Cloud Format
- `CC-Module-Feature.md` - Main format
- Examples: `AP-invoice.md`, `gl-journal_voucher.md`, `AR-receipt.md`

### BlueLedgers Format
- `M-Feature.md` - Material module
- `P-Feature.md` - Procurement module
- `O-Feature.md` - Options module
- Examples: `M-Stock In.md`, `P-Purchase Order.md`

### Training Center Format
- `module-indexN.md` - Training materials
- Examples: `ap-index1.md`, `gl-index3.md`

---

## Standard Document Structure

### Frontmatter Schema
```yaml
---
title: "Thai title"
title_en: "English title"  # often missing
lang: th-TH
module: carmen_cloud
submodule: ap|ar|gl|asset|configuration|workbook
doc_type: procedure|configuration|troubleshooting|reference
---
```

### Content Sections
1. **Title** - Thai heading with English subtitle
2. **Introduction** - Brief purpose description
3. **Step-by-step procedures** - Numbered instructions
4. **Field descriptions** - Table format with Thai labels
5. **Screenshots** - `![alt text](image-XX.png)` format
6. **Video tutorials** - Embedded YouTube iframes
7. **Copy/Template functions** - Re-creation methods

---

## Inter-Module Workflows

### Procure-to-Pay Flow
```
Purchase Order (BlueLedgers)
    → Goods Receiving (BlueLedgers)
        → AP Invoice (Carmen Cloud)
            → AP Payment (Carmen Cloud)
                → Posting to GL (Carmen Cloud)
```

### Order-to-Cash Flow
```
AR Invoice (Carmen Cloud)
    → AR Receipt (Carmen Cloud)
        → Posting to GL (Carmen Cloud)
```

### Asset Lifecycle
```
Asset Register
    → Monthly Depreciation
        → Disposal/Transfer
            → Posting to GL
```

### Period End Process
```
1. Complete all module transactions
2. Post from sub-ledgers (AP, AR, Asset) to GL
3. Review Journal Vouchers
4. Close Period (AP, AR, Asset)
5. Year End Close (GL)
```

---

## Common Patterns in Documentation

### Step Numbering
- Format: `1.1`, `1.2`, `2.1`, `2.2`
- Major sections: `1.`, `2.`, `3.`
- Sub-sections: `1.1.1`, `1.1.2`

### Required Fields
- Marked with asterisk `*` or `*`
- Text: "(สัญลักษณ์ * ช่องที่จำเป็นต้องระบุ)"

### Button References
- Format: `**<span class="btn">BUTTON_NAME</span>**`
- Icons: `<img src="/public/add_icon.png" />`

### Video References
- Format: `<iframe src="https://www.youtube.com/embed/VIDEO_ID"></iframe>`
- Usually at end of document

---

## Account Nature (Thai Chart of Accounts)

| หมวด | Nature | Normal Balance | English |
|------|--------|----------------|---------|
| หมวด 1 | Assets | Debit | สินทรัพย์ |
| หมวด 2 | Liabilities | Credit | หนี้สิน |
| หมวด 3 | Equity | Credit | ทุน |
| หมวด 4 | Revenue | Credit | รายได้ |
| หมวด 5 | Expenses | Debit | ค่าใช้จ่าย |

---

## Tax Status Values (AP Module)

| Status | Thai | English | GL Entry Impact |
|--------|------|---------|-----------------|
| Confirm | ยืนยัน | Confirmed | Post to Input Tax account immediately |
| Pending | รอชำระ | Pending | Post to Temporary account, reconcile later |
| Unclaim | ไม่ขอคืน | Cannot claim | Post to non-deductible account |
| None | ไม่มีภาษี | No tax | No tax account involved |

---

## Copy Function Patterns

Most modules support copy operations with these variants:
- **Copy to new** - Duplicate as new document
- **Copy and reverse** - Duplicate with Dr/Cr swapped
- **Copy with zero amount** - Template without amounts
- **Copy to template** - Save as reusable template

---

## Key Integration Points

### AP → GL
- AP Invoice → Dr: Expense, Cr: AP
- AP Payment → Dr: AP, Cr: Cash/Bank
- Tax Reconciliation → Adjusts Input Tax

### AR → GL
- AR Invoice → Dr: AR, Cr: Revenue
- AR Receipt → Dr: Cash/Bank, Cr: AR
- Debit/Credit Note → Adjusts AR and Revenue

### Asset → GL
- Asset Register → Dr: Asset, Cr: AP/Cash
- Monthly Depreciation → Dr: Depreciation, Cr: Accumulated Depreciation

### Inventory → GL
- Stock In → Dr: Inventory, Cr: AP
- Stock Out → Dr: COGS, Cr: Inventory

---

## File Locations for Reference

### Main Documentation
- AP: `docs/carmen_cloud/ap/*.md`
- AR: `docs/carmen_cloud/ar/*.md`
- GL: `docs/carmen_cloud/gl/*.md`
- Asset: `docs/carmen_cloud/asset/*.md`
- Configuration: `docs/carmen_cloud/configuration/*.md`
- Workbook: `docs/carmen_cloud/workbook/*.md`

### Training Materials
- `docs/training_center/carmen_cloud/`

### Images
- `docs/_images/[month][year]/`

### Changelogs
- `docs/changelog/[month][year].md`

---

## Common User Queries (Thai)

1. "วิธีสร้างใบแจ้งหนี้ AP" - How to create AP invoice
2. "วิธีโพสต์ AP เข้า GL" - How to post AP to GL
3. "วิธีคำนวณค่าเสื่อม" - How to calculate depreciation
4. "วิธีทำ reconciliation ภาษี" - How to do tax reconciliation
5. "วิธีปิดงวดบัญชี" - How to close accounting period
6. "วิธีสร้าง JV" - How to create journal voucher
7. "วิธีออกใบกำกับภาษี" - How to issue tax invoice
8. "วิธีรับสินทรัพย์" - How to receive assets

---

## Common User Queries (English)

1. "How to create AP invoice"
2. "How to post to GL"
3. "How to calculate depreciation"
4. "How to reconcile tax"
5. "How to close period"
6. "How to create journal voucher"
7. "How to issue tax invoice"
8. "Asset registration process"

---

## Known Issues in Documentation

### Content Duplicates
- `AP-RDPrep_3.md` ≈ `AP-RDPrep_53.md` - Same content, different form number

### Empty Files
- `carmen_cloud/index.md` - Needs module overview

### Missing Content
- No module overview/introduction documents
- No troubleshooting guides
- No end-to-end workflow documentation
- Limited cross-references between modules

### Format Issues
- Inconsistent frontmatter
- Mixed Thai/English without clear structure
- Image paths may be broken
- Video iframes not searchable

---

## RAG Implementation Notes

### Language Strategy
- **Primary**: Thai (lang: th-TH)
- **Secondary**: English (UI labels, titles)
- **Approach**: Thai-first with English query translation fallback

### Chunking Priorities
1. Keep complete procedures together
2. Preserve table captions with data
3. Include field descriptions with their context
4. Extract video metadata as separate chunks

### Search Tags
- Module: `ap`, `ar`, `gl`, `asset`, `configuration`, `workbook`
- Function: `invoice`, `payment`, `reconciliation`, `posting`, `depreciation`
- Country: `thailand`, `philippines`, `generic`
- Content type: `procedure`, `reference`, `troubleshooting`, `video`

---

## Agent Usage Guidelines

When helping users with Carmen Cloud:

1. **Always identify the module** first (AP, AR, GL, Asset)
2. **Check the country context** (Thailand vs Philippines) for tax matters
3. **Understand the workflow** - Is this a new transaction or correction?
4. **Provide step-by-step guidance** with reference to specific document sections
5. **Consider integration points** - Does this affect other modules?
6. **Highlight tax implications** - VAT, WHT, and reconciliation requirements
7. **Reference related documents** - Cross-module workflows may be relevant

---

## Version Information

- **System**: Carmen Cloud
- **Documentation Period**: May 2024 - November 2025
- **Primary Language**: Thai
- **Target Regions**: Thailand, Philippines
- **Last Updated**: 2025-01-15

---

## Quick Reference Links

- [AP Invoice Documentation](carmen_cloud/ap/AP-invoice.md)
- [Journal Voucher Documentation](carmen_cloud/gl/c-journal_voucher.md)
- [Asset Register Documentation](carmen_cloud/asset/AS-asset_register.md)
- [Chart of Accounts](carmen_cloud/configuration/CF-chart_of_account.md)
- [AR Invoice Documentation](carmen_cloud/ar/AR-invoice.md)
- [Posting AP to GL](carmen_cloud/gl/c-posting_ap.md)
- [Posting AR to GL](carmen_cloud/gl/c-posting_ar.md)
