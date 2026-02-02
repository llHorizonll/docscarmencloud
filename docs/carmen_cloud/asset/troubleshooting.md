---
title: "Asset Module Troubleshooting"
title_en: "Asset Management Troubleshooting Guide"
lang: th-TH
module: carmen_cloud
submodule: asset
doc_type: troubleshooting
complexity: intermediate
tags: [asset, troubleshooting, error, fixed_asset, depreciation]
country_specific: generic
target_audience: accountant
---

# Asset Management - แก้ปัญหา (Troubleshooting Guide)

## ปัญหาที่พบบ่อย (Common Issues)

---

## 1. บันทึก Asset (ทรัพย์สิน) ไม่สำเร็จ

### Error Messages:
- "Cannot save asset"
- "Required field is missing"
- "Invalid date"
- "Account code is required"

### Solutions:

#### 1.1 ตรวจสอบ Required Fields (มีเครื่องหมาย *)
```
✓ Asset No (รหัสทรัพย์สิน)
✓ Asset Name (ชื่อทรัพย์สิน)
✓ Input Date (วันที่นำเข้าสู่ระบบ)
✓ Acquire Date (วันที่ได้มา)
✓ Category (หมวดหมู่)
✓ Department (แผนก)
✓ Location (สถานที่)
✓ Currency (สกุลเงิน)
✓ Rate (อัตราแลกเปลี่ยน)
✓ Amount/Unit (ราคาต่อหน่วย)
✓ Unit (หน่วย)
✓ Qty (จำนวน)
✓ Asset Life (อายุการใช้งาน)
```

#### 1.2 ตรวจสอบ Input Date vs Acquire Date
```
Input Date = วันที่ระบบเริ่มคำนวณค่าเสื่อม
Acquire Date = วันที่ได้ทรัพย์สินมาจริง

กฎ: Acquire Date ต้องน้อยกว่าหรือเท่ากับ Input Date
ถ้า Acquire Date > Input Date → ระบบจะไม่ให้บันทึก
```

#### 1.3 ตรวจสอบ Account Code
```
ต้องระบุ Account Code ในส่วน:
✓ Cost Account (บัญชีต้นทุน)
✓ Accum. Depreciation (บัญชีค่าเสื่อมสะสม)
✓ Depreciation Account (บัญชีค่าเสื่อม)
```

---

## 2. คำนวณค่าเสื่อมไม่ถูกต้อง

### ปัญหา:
- ค่าเสื่อมรายเดือนไม่ตรงตามที่ควรจะเป็น
- ค่าเสื่อมสะสมไม่ถูกต้อง

### Solutions:

#### 2.1 สูตรการคำนวณค่าเสื่อม
```
Monthly Depreciation =
((Cost - Accumulated Depreciation - Salvage Value) / Total Asset Life in Days)
× Days in Month

ปัจจัยที่ส่งผล:
- Cost (ต้นทุน)
- Accumulated Depreciation (ค่าเสื่อมสะสม)
- Salvage Value (ราคาซาก)
- Asset Life (อายุการใช้งาน)
- Input Date และ Acquire Date
```

#### 2.2 ตรวจสอบ Asset Life Setup
```
Asset Life ต้องระบุเป็น:
✓ Year (ปี)
✓ Month (เดือน)
✓ Day (วัน)

ระบบจะคำนวณเป็นจำนวนวันทั้งหมด
และคำนวณค่าเสื่อมรายเดือนตามจำนวนวันในเดือนนั้นๆ
```

#### 2.3 ดูประวัติการคำนวณ
```
Asset Register → เลือก Asset → Tab "History Depreciation"
จะแสดง:
- ค่าเสื่อมรายเดือน
- ค่าเสื่อมสะสม
- วันที่คำนวณ
```

---

## 3. ทำ Asset Disposal (จำหน่าย/ทิ้ง) ไม่ได้

### Error Messages:
- "Cannot dispose asset"
- "Asset not eligible for disposal"
- "Account code not configured"

### Solutions:

#### 3.1 ตรวจสอบวิธี Disposal
```
ระบบรองรับเฉพาะ:
- Disposal แบบ Quantity (จำนวน)

ยังไม่รองรับ Disposal แบบ Amount (จำนวนเงิน)
```

#### 3.2 ตรวจสอบ Account Code สำหรับ Disposal
```
ต้องตั้งค่า Account Code ดังนี้:
✓ Asset Account (Credit) → ลดมูลค่าทรัพย์สิน
✓ Accum. Account (Debit) → ลดค่าเสื่อมสะสม
✓ Gain/Loss Account → บันทึกกำไร/ขาดทุน
✓ Sale Account (Debit) → บันทึกเงินสด/ธนาคารที่ได้รับ
```

#### 3.3 สร้าง Disposal
```
1. Asset Module → Function → Asset Disposal
2. เลือก Asset ที่ต้องการ Disposal
3. ระบุจำนวน (Quantity) ที่จะ Disposal
4. ระบุวันที่ Disposal
5. ระบุราคาขาย (ถ้ามี)
6. กด Confirm

ระบบจะสร้าง Journal Entry อัตโนมัติ
```

---

## 4. Pre-Register Asset ดึงข้อมูลไม่ได้

### Error Messages:
- "Cannot pull data from AP"
- "Cannot pull data from Receiving"
- "Account code not configured"

### Solutions:

#### 4.1 ตั้งค่า Asset Account Code ก่อนใช้งาน
```
Setting → Asset → "Set Asset Account Code for Posting"

เลือกเฉพาะ Account Code ที่เกี่ยวข้องกับ Asset
ห้ามกด Select All เพราะจะดึงรายการที่ไม่ใช่ Asset มาด้วย
```

#### 4.2 เลือก Source ที่จะดึงข้อมูล
```
เลือกได้ 2 ทาง:
1. Posting from Accounts Payable (AP)
   - ดึงจาก AP Invoice ที่ยังไม่ได้ Register

2. Posting from Receiving
   - ดึงจาก Receiving Module

เลือกใช้เพียง 1 วิธีตามการทำงานของบริษัท
```

#### 4.3 ตรวจสอบสถานะของรายการ
```
- รายการที่ Posted แล้ว → ดึงมาเป็น Asset ได้
- รายการที่ Void → ไม่สามารถดึงมาได้

สถานะรายการ:
- Draft → สามารถ Void ได้
- Void → สามารถ Un-Void กลับเป็น Draft ได้
```

---

## 5. Asset Checker (Mobile Scan) ใช้งานไม่ได้

### ปัญหา:
- แสกน QR Code ไม่ได้
- ถ่ายรูป Asset ไม่ได้
- ไม่แสดงพิกัด GPS

### Solutions:

```
1. ตรวจสอบ Browser Permissions
   - อนุญาตให้เข้าถึง Camera
   - อนุญาตให้เข้าถึง Storage
   - อนุญาตให้เข้าถึง Location (GPS)

2. ใช้ Chrome Browser บน Mobile หรือ Tablet

3. พิมพ์ QR Code:
   - Asset Module → Reports → Asset QR Code List
   - เลือก Asset ที่ต้องการ
   - กด Print

4. การถ่ายรูป Asset:
   - Click ที่รูป Asset Photo
   - เลือกถ่ายรูปใหม่ หรือใช้รูปเดิม
   - รูปจะถูกอัปโหลดไปยังระบบ

5. การติดตามพิกัด:
   - เปิด Location Service บนเครื่อง
   - ระบบจะบันทึกพิกัดอัตโนมัติเมื่อแสกน
```

---

## 6. Transfer Asset (ย้ายสถานที่) ไม่ได้

### ปัญหา:
- แก้ไข Location หรือ Department ไม่ได้
- Transfer History ไม่แสดง

### Solutions:

```
1. สำหรับ Asset ใน Period ที่เปิดอยู่:
   - เปิด Asset Register
   - แก้ไข Location และ Department ได้เลย
   - ระบบจะบันทึกประวัติโดยอัตโนมัติ

2. สำหรับ Asset ใน Period ที่ปิดแล้ว:
   - สามารถแก้ไขได้เฉพาะ:
     ✓ Department
     ✓ Location
     ✓ Transfer Date
   - ไม่สามารถแก้ไขรายการอื่นได้

3. ดูประวัติการย้าย:
   - Tab "History Location"
   - แสดงการย้ายตามลำดับเวลา
```

---

## 7. ปิด Asset Period ไม่ได้

### Error Messages:
- "Cannot close period"
- "There are incomplete data"

### Solutions:

```
1. ตรวจสอบความสมบูรณ์ของข้อมูล:
   - Asset ทั้งหมดถูกบันทึกแล้ว
   - ค่าเสื่อมรายเดือนคำนวณแล้ว
   - Disposal ทำเรียบร้อยแล้ว

2. Asset Period Closure:
   - ส่งผลเฉพาะ Asset Management Module
   - ยังสามารถ Post ไป GL ได้ (ถ้า GL Period ยังเปิด)

3. การเปิด Period ที่ปิดแล้ว:
   - ติดต่อ FC, Account Manager หรือผู้มีอำนาจ
   - ส่งอีเมลแจ้ง Support
   - ระบุเหตุผลและ Period ที่ต้องการเปิด
```

---

## 8. Print QR Code ไม่ได้

### ปัญหา:
- ไม่สามารถพิมพ์ QR Code สำหรับแปะทรัพย์สิน

### Solutions:

```
1. ตรวจสอบ Printer:
   - ใช้ Printer ที่รองรับ Windows Driver
   - ใช้กระดาษสติกเกอร์ขนาดตามต้องการ

2. เข้าถึงผ่าน:
   - Asset Module → Reports → Asset QR Code List

3. เลือก Asset:
   - เลือกทั้งหมด หรือ เลือกเฉพาะที่ต้องการ
   - กด Print

4. ตั้งค่า Printer:
   - เลือกขนาดกระดาษ
   - เลือกความละเอียด
   - กด Print
```

---

## Quick Checklist ก่อนแจ้งปัญหา

```
[ ] ตรวจสอบ Required Fields ครบถ้วน
[ ] ตรวจสอบ Input Date >= Acquire Date
[ ] ตรวจสอบ Account Code ถูกต้อง
[ ] ตรวจสอบ Asset Life ถูกต้อง
[ ] ตรวจสอบ Internet Connection เชื่อมต่ออยู่
[ ] ตรวจสอบว่า Asset อยู่ใน Period ที่เปิดอยู่
```

---

## ติดต่อ Support

หากทำตามขั้นตอนแล้วยังไม่หาย:

1. **Screenshot Error** ที่แสดง
2. **ระบุ Module:** Asset Module
3. **ระบุ Function:** บันทึก Asset / Disposal / Transfer
4. **ระบุขั้นตอนที่ทำแล้ว** (Steps taken)
5. **ติดต่อ Admin:** แจ้งระบบลูกค้า
