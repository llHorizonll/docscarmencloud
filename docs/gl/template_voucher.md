---
title: Template Voucher
lang: th-TH
---

# Template Voucher

Function นี้ใช้เพื่อสร้างแม่แบบเอกสารที่มีการบันทึกอยู่เป็นประจำ เพื่อช่วยลดปริมาณการบันทึกข้อมูลใน JV และลดความผิดพลาดในการเลือกรหัสบัญชีผิด
การสร้าง Template สามารถสร้างได้ 2 วิธี

## การสร้าง Template บนหน้าจอ Template Voucher

มีขั้นตอนการบันทึกดังนี้

1.1. Click เข้าสู่ General Ledger Module

1.2. Click เลือก Template Voucher

1.3. กดปุ่ม <img src="../add_icon.png" style="display: inline-block;" />

![alt text](image-25.png)

1.4. ใส่ข้อมูลประเภทสมุดบัญชี (Prefix) และระบุรายละเอียดชื่อ Template

- Prefix กำหนด Prefix ที่ต้องการสร้าง Template
- Type ระบบจะกำหนดค่า “Template” ให้อัตโนมัติ
- Description กำหนดคำอธิบายที่ต้องการให้แสดงใน JV Description

  1.5. Click เครื่องหมาย + เพื่อเพิ่มรายการที่จะใช้บันทึกบัญชี

![alt text](image-26.png)

1.6. ระบบจะแสดงหน้าต่าง ดังภาพด้านล่าง ให้ระบุข้อมูลดังต่อไปนี้

**หมายเหตุ** เครื่องหมาย <span class="asterisk">\*</span>
(สัญลักษณ์ \* ช่องที่จำเป็นต้องระบุ)

- <span class="asterisk">\*</span> Department กำหนด Department Code
- <span class="asterisk">\*</span> Account # กำหนด Account code
- Comment คำอธิบายรายการ
- <span class="asterisk">\*</span> Currency กำหนด Currency Code
- <span class="asterisk">\*</span> Rate กำหนด Currency Rate
- Amount Dr / Amount Cr ใส่ยอดที่ต้องการบันทึก
- Dimension ใส่ข้อมูล Dimension (ถ้ามี)

---

1.7. หลังจากระบุข้อมูลเรียบร้อยแล้วให้ กด **<span class="btn">OK</span>**

![alt text](image-27.png)

1.8. เมื่อเพิ่มรายการจนครบตามที่ต้องการแล้วให้กดปุ่ม **<span class="btn">SAVE</span>** เพื่อบันทึก Template

![alt text](image-28.png)

1.9. กด **<span class="btn">OK</span>** เพื่อเสร็จสิ้นการบันทึกข้อมูล

<p align="center">
    <img src="./image-15.png"  />
</p>

1.10. การใช้งานปุ่มอื่น ๆ หน้าจอ

<img src="../add_icon.png" style="display: inline-block;" /> สร้างเอกสารแม่แบบ

<img src="../edit_icon.png" style="display: inline-block;" /> แก้ไขเอกสารแม่แบบ

<img src="../del_icon.png" style="display: inline-block;" /> การยกเลิกเอกสารแม่แบบ

<img src="../print_icon.svg" style="display: inline-block;" /> พิมพ์เอกสาร

## การสร้าง Template จากการ Copy บนหน้าจอ Journal Voucher

**การคัดลอก JV โดยใช้คำสั่ง Copy to Template** ใช้ในกรณีที่ต้องการสร้างเอกสารสมุดบัญชีแม่แบบ (Template) จากสมุดบัญชีที่ได้บันทึกไว้ก่อนแล้ว

2.1 Click เข้าสู่ General Ledger Module

2.2 เลือกเมนู Journal Voucher

2.3 Click สัญลักษณ์ <img src="./image-29.png" style="display: inline-block;" /> ใน JV ที่ต้องการจะทำการคัดลอก

![alt text](image-30.png)

2.4 ระบบจะเปิด JV ที่เลือกมา
2.5 Click <img src="../copy_icon.png" style="display: inline-block;" />

![alt text](image-31.png)

2.6 เลือก Copy to Template

<p align="center">
    <img src="./image-32.png"  />
</p>

2.7 Click **<span class="btn">OK</span>** เพื่อยืนยันการคัดลอก ระบบจะสร้างเอกสาร JV ขึ้นเป็นแม่แบบ

<p align="center">
    <img src="./image-4.png"  />
</p>

2.8 ระบบสร้างแม่แบบขึ้นอัตโนมัติเพื่อสามารถนำไปใช้เป็นแม่แบบในการบันทึกบัญชี สามารถดูเอกสารที่ function ชื่อ Template Voucher

![alt text](image-33.png)

การใช้งานปุ่มอื่น ๆ บนหน้าจอ

3.1 กดปุ่ม <img src="../search_icon.svg" style="display: inline-block;" /> เพื่อค้นหา Template Voucher

3.2 กดปุ่ม <img src="../cloud_download_icon.svg" style="display: inline-block;" /> เพื่อ Export ข้อมูลออกจากระบบเป็น .csv

3.3 กดปุ่ม <img src="../print_icon.svg" style="display: inline-block;" /> เพื่อพิมพ์ข้อมูล
