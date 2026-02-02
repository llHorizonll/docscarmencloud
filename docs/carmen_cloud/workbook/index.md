---
title: "Carmen Workbook Module"
title_en: "Carmen Workbook Module Guide"
lang: th-TH
module: carmen_cloud
submodule: workbook
doc_type: overview
complexity: beginner
tags: [workbook, overview, excel, add-in]
country_specific: generic
target_audience: accountant
---

# Carmen Workbook Module

## ภาพรวม (Overview)

**Carmen Workbook** คือ Excel Add-in ที่เชื่อมต่อระบบ Carmen Cloud กับ Microsoft Excel เพื่อ:
- ดึงข้อมูลรายงานต่าง ๆ จากระบบ (Balance Sheet, P&L, Trial Balance, etc.)
- อัปโหลด Transaction (JV, Budget) เข้าระบบ
- ทำงานกับข้อมูลลูกค้าใน Excel ได้อย่างสะดวก

---

## เอกสาร (Documents)

| เอกสาร | คำอธิบาย |
|---------|-----------|
| [Install & Config](./WB-install&config.md) | วิธีติดตั้งและตั้งค่าก่อนใช้งาน |
| [Workbook Functions](./WB-function.md) | ฟังก์ชันและวิธีการใช้งานต่าง ๆ |
| [Troubleshooting](./troubleshooting.md) | แก้ปัญหาที่พบบ่อย |

---

## ปัญหาที่พบบ่อย (Common Issues)

### กด Refresh ไม่ได้

**สาเหตุ:** ไฟล์ Excel ยังไม่ถูก Unblock หรือ Add-in ยังไม่ได้เปิดใช้งาน

**วิธีแก้ไข:**
1. Click ขวาที่ไฟล์ > Properties > ติ๊ก Unblock
2. ตรวจสอบ Carmen Add-in ถูกเปิดใช้งาน (File > Options > Add-Ins)
3. ดูรายละเอียดเพิ่มใน [Troubleshooting Guide](./troubleshooting.md)

---

## ขั้นตอนการเริ่มใช้งาน (Getting Started)

1. **ติดตั้ง Carmen Add-in**
   - ดาวนโหลดจาก `/carmen.api`
   - ติดตั้ง Excel Add-in (x32/x64)
   - ติดตั้ง Application Configuration

2. **ตั้งค่า Excel Security**
   - เปิดใช้งาน Macro
   - เพิ่ม Carmen Add-in
   - Unblock ไฟล์ Excel

3. **เชื่อมต่อระบบ**
   - ไปที่ Tab "Carmen Add-in"
   - กด "Config WebAPI"
   - Login ด้วย username/password

4. **เริ่มใช้งาน**
   - กด Refresh เพื่อดึงข้อมูล
   - กด Recalculate All Sheets เพื่ออัปเดต
   - Upload Transaction ได้

---

## Video Tutorial

<p style="margin: 0;">Video ประกอบ</p>
<h3 style="margin: 0;">Setup | การตั้งค่าก่อนเริ่มใช้งาน</h3>

<iframe width="560" height="315" src="https://www.youtube.com/embed/Y42UT8szy-M?si=8PvPXm1nOeV5OAWk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## ติดต่อ Support

- คู่มือออนไลน์: https://xxxxx.carmen.blue
- Email: xxxxx@carmen.blue
