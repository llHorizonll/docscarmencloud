import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "CARMEN",
  description: "Document for carmen.blue",
  head: [["link", { rel: "icon", href: "/favicon.ico" }]],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      {
        text: "Changelog",
        items: [
          {
            text: "🆕 September2025 Relaese Infomation",
            link: "/sep2025",
          },
          {
            text: "Jul2025 Relaese Infomation",
            link: "/jul2025",
          },
          {
            text: "May2025 Relaese Infomation",
            link: "/may2025",
          },
          {
            text: "April2025 Relaese Infomation",
            link: "/apr2025",
          },
          {
            text: "March2025 Relaese Infomation",
            link: "/mar2025",
          },
          {
            text: "January2025 Relaese Infomation",
            link: "/jan2025",
          },
          {
            text: "November2024 Relaese Infomation",
            link: "/nov2024",
          },
          {
            text: "August2024 Relaese Infomation",
            link: "/aug2024",
          },
          {
            text: "June2024 Relaese Infomation",
            link: "/june2024",
          },
          {
            text: "May2024 Relaese Infomation",
            link: "/may2024",
          },
          {
            text: "Changelog",
            link: "/changelog/index",
            activeMatch: "/changelog/",
          },
        ],
      },
      // { text: "Examples", link: "/markdown-examples" },
    ],
    sidebar: {
      "/carmen_cloud/": { base: "/carmen_cloud/", items: sidebarAll() },
      "/training_center/": { base: "/training_center/carmen_cloud/", items: sidebarTraining() },
      "/carmen_onpermise/": { base: "/training_center/carmen_onpermise/", items: sidebarTraining() },
      "/Blueledgers/": { base: "/Blueledgers/", items: sidebarBL() },
    },

    socialLinks: [{ icon: "github", link: "https://github.com/llHorizonll/docscarmencloud" }],
    search: {
      provider: "local",
    },
  },
  cacheDir: "./.vitepress/.vite",
});

function sidebarAll() {
  return [
    {
      text: "Dashboard",
      link: "/dashboard",
    },
    {
      text: "General Ledger",
      collapsed: true,
      base: "/carmen_cloud/gl/c-",
      items: [
        { text: "Journal Voucher", link: "journal_voucher" },
        { text: "Template Voucher", link: "template_voucher" },
        { text: "Recurring Voucher", link: "recurring_voucher" },
        { text: "Amortization Voucher", link: "amortization_voucher" },
        { text: "Allocation Voucher", link: "allocation_voucher" },
        { text: "Budget", link: "budget" },
        { text: "Posting Account Payable to GL", link: "posting_ap" },
        { text: "Posting Account Receivable to GL", link: "posting_ar" },
        { text: "Inventory & Extra Cost Posting to GL", link: "posting_inventory" },
        { text: "Posting Fixed Assets to GL", link: "posting_asset" },
        { text: "Close Period and Year End", link: "close_period" },
        { text: "Financial Report", link: "FinancialGL" },
      ],
    },
    {
      text: "Account Payable",
      collapsed: true,
      base: "/carmen_cloud/ap/AP-",
      items: [
        { text: "Vendor", link: "vendor" },
        { text: "Posting AP invoice from recieving", link: "recevingToAp" },
        { text: "Invoice", link: "invoice" },
        { text: "Payment", link: "payment" },
        { text: "Deposit Payment", link: "deposit_payment" },
        { text: "Apply Deposit with Invoice", link: "apply_deposit_pay_with_inv" },
        { text: "Cheque Reconciliation", link: "cheque_reconciliation" },
        { text: "Input Tax Reconciliation", link: "input_tax_reconciliation" },
        { text: "WHT Reconciliation", link: "wht_reconciliation" },
        { text: "RDPrep_การโอนย้ายข้อมูลใบแนบ ภงด 3", link: "RDPrep_3" },
        { text: "RDPrep_การโอนย้ายข้อมูลใบแนบ ภงด 53", link: "RDPrep_53" },
        { text: "Close Period AP", link: "close_period" },
      ],
    },
    {
      text: "Account Receivable",
      collapsed: true,
      base: "/carmen_cloud/ar/AR-",
      items: [
        { text: "Profile", link: "profile" },
        { text: "AR Posting from PMS (PMS Interface)", link: "posting_pms" },
        { text: "Folio", link: "folio" },
        { text: "Invoice", link: "invoice" },
        { text: "Contract", link: "contract" },
        { text: "Apply AR Contract", link: "apply_contract" },
        { text: "Receipt", link: "receipt" },
        { text: "Receipt for Advance Deposit", link: "receipt_advance_deposit" },
        { text: "Apply invoice for Advance Deposit", link: "apply_invoice_advance_deposit" },
        { text: "Close Period AR", link: "close_period" },
      ],
    },
    {
      text: "Asset",
      collapsed: true,
      base: "/carmen_cloud/asset/AS-",
      items: [
        { text: "Pre-Register Asset Setting", link: "preasset_setting" },
        { text: "Pre-Register Asset", link: "preasset" },
        { text: "Asset Register", link: "asset_register" },
        { text: "Print Asset QR Code", link: "print_asset" },
        { text: "Asset Disposal", link: "asset_disposal" },
        { text: "Asset Checker", link: "asset_checker" },
        { text: "Close Period Asset", link: "close_period" },
      ],
    },
    {
      text: "Comment and Document Management & Activity Log",
      collapsed: true,
      base: "/carmen_cloud/comment/CM-",
      items: [{ text: "Comment and Document Management & Activity Log", link: "index" }],
    },

    {
      text: "Work Book",
      collapsed: true,
      base: "/carmen_cloud/workbook/WB-",
      items: [
        { text: "Installation and Configuration", link: "install&config" },
        { text: "Work Book Function", link: "function" },
        { text: "Excel Security setting for Carmen Add-in", link: "excelsecurity" },
        { text: "Troubleshoot Guide", link: "troubleshootguide" },
      ],
    },
    {
      text: "Configuration",
      collapsed: true,
      base: "/carmen_cloud/configuration/CF-",
      items: [
        { text: "Product License", link: "product_license" },
        { text: "Company Profile", link: "company_profile" },
        { text: "System Preference", link: "system_preference" },
        { text: "Users", link: "users" },
        { text: "Change Password User", link: "change_password_user" },
        { text: "Permissions", link: "permissions" },
        { text: "Currency Exchange Rate", link: "currency_exrate" },
        { text: "Currency", link: "currency" },
        { text: "Department", link: "department" },
        { text: "Chart Of Accounts", link: "chart_of_account" },
        { text: "Payment Type", link: "payment_type" },
        { text: "Dimension", link: "dimension" },
        { text: "Unit", link: "unit" },
      ],
    },
  ];
}

function sidebarTraining() {
  return [
    {
      text: "Carmen Cloud",
      collapsed: false,
      items: [
        {
          text: "Account Payable",
          collapsed: true,
          base: "/training_center/carmen_cloud/AP/ap-",
          items: [
            {
              text: "Vendor Profile",
              link: "index",
            },
            {
              text: "Invoice",
              link: "index1",
            },
            {
              text: "Payment",
              link: "index2",
            },
            {
              text: "Input Vat Reconciliation",
              link: "index3",
            },
            {
              text: "Withholding Tax Reconciliation",
              link: "index4",
            },
          ],
        },
        {
          text: "Account Receivable",
          collapsed: true,
          base: "/training_center/carmen_cloud/AR/ar-",
          items: [
            {
              text: "Customer(AR)Profile",
              link: "index1",
            },
            {
              text: "Invoice",
              link: "index2",
            },
            {
              text: "Create Invoice from City Ledger Folio",
              link: "index3",
            },
            {
              text: "Receipt",
              link: "index4",
            },
          ],
        },
        {
          text: "Fixed Asset",
          collapsed: true,
          base: "/training_center/carmen_cloud/Fixed Asset/asset-",
          items: [
            {
              text: "Asset Registration",
              link: "index1",
            },
            {
              text: "Batch Asset Registration",
              link: "index2",
            },
            {
              text: "Disposal Asset",
              link: "index3",
            },
          ],
        },
        {
          text: "Asset Checker",
          collapsed: true,
          base: "/training_center/carmen_cloud/Asset Checker/ac-",
          items: [
            {
              text: "Mobile Asset Checking ",
              link: "index1",
            },
          ],
        },
        {
          text: "General Ledger",
          collapsed: true,
          base: "/training_center/carmen_cloud/General_Ledger/gl-",
          items: [
            {
              text: "Journal Voucher",
              link: "index",
            },
            {
              text: "Copy Function on JV",
              link: "index1",
            },
            {
              text: "Create and Apply Template Voucher",
              link: "index2",
            },
            {
              text: "Allocation Voucher ",
              link: "index3",
            },
            {
              text: "Recurring Voucher",
              link: "index4",
            },
            {
              text: "Amortization Voucher",
              link: "index5",
            },
            {
              text: "Budget",
              link: "index6",
            },
            {
              text: "Posting from Other Modules",
              link: "index7",
            },
            {
              text: "Year Ending",
              link: "index8",
            },
            {
              text: "Financial Report",
              link: "index9",
            },
          ],
        },
        {
          text: "Work Book",
          collapsed: true,
          base: "/training_center/carmen_cloud/Work_Book/wb-",
          items: [
            {
              text: "Set up a business unit (BU)",
              link: "index1",
            },

            {
              text: "How to upload a journal voucher (JV) from excel",
              link: "index2",
            },

            {
              text: "How to upload JV allocation from excel",
              link: "index3",
            },

            {
              text: "How to upload a budget from excel",
              link: "index4",
            },

            {
              text: "Excel Security setting for Carmen Add-in",
              link: "index5",
            },
          ],
        },
      ],
    },
    {
      text: "Carmen On-Permise",
      collapsed: false,
      items: [
        {
          text: "Inventory",
          collapsed: true,
          base: "/training_center/carmen_onpermise/INVENTORY/iv-",
          items: [
            {
              text: "Receiving",
              link: "index1",
            },

            {
              text: "Requisition",
              link: "index2",
            },

            {
              text: "Transfer",
              link: "index3",
            },

            {
              text: "Issue",
              link: "index4",
            },

            {
              text: "Adjustment / Sale",
              link: "index5",
            },

            {
              text: "Stock count and Close period",
              link: "index6",
            },

            {
              text: "Report",
              link: "index7",
            },
          ],
        },
        {
          text: "Recipe",
          collapsed: true,
          base: "/training_center/carmen_onpermise/RECIPE/re-",
          items: [
            {
              text: "Recipe",
              link: "index",
            },
          ],
        },
        {
          text: "Asset Management",
          collapsed: true,
          base: "/training_center/carmen_onpermise/ASSET/s-",
          items: [
            {
              text: "Asset Register",
              link: "index1",
            },

            {
              text: "Depreciation calculation",
              link: "index2",
            },

            {
              text: "Asset Disposal",
              link: "index3",
            },

            {
              text: "Report",
              link: "index4",
            },
          ],
        },
        {
          text: "General Ledger",
          collapsed: true,
          base: "/training_center/carmen_onpermise/GlONPERMISE/g-",
          items: [
            {
              text: "Chart of Account",
              link: "index1",
            },

            {
              text: "Budget",
              link: "index2",
            },

            {
              text: "Journal Voucher",
              link: "index3",
            },

            {
              text: "Standard Voucher (Recurring) and Data Posting",
              link: "index4",
            },

            {
              text: "Close Period and Year End",
              link: "index5",
            },

            {
              text: "Report",
              link: "index6",
            },
          ],
        },
        {
          text: "Add In",
          collapsed: true,
          base: "/training_center/carmen_onpermise/Addin/add-",
          items: [
            {
              text: "Financial Report",
              link: "index1",
            },
          ],
        },
        {
          text: "Account Payable",
          collapsed: true,
          base: "/training_center/carmen_onpermise/ApONPERMISE/a-",
          items: [
            {
              text: "Cloud Highlight",
              link: "index1",
            },

            {
              text: "Vendor",
              link: "index2",
            },

            {
              text: "Invoice",
              link: "index3",
            },

            {
              text: "Payment",
              link: "index4",
            },

            {
              text: "Procedure",
              link: "index5",
            },

            {
              text: "Report",
              link: "index6",
            },
          ],
        },
        {
          text: "Account Receivable",
          collapsed: true,
          base: "/training_center/carmen_onpermise/ArONPERMISE/r-",
          items: [
            {
              text: "AR Profile",
              link: "index1",
            },

            {
              text: "Invoice",
              link: "index2",
            },

            {
              text: "Receipt",
              link: "index3",
            },

            {
              text: "Report",
              link: "index4",
            },
          ],
        },
      ],
    },
    {
      text: "Cadena",
      collapsed: false,
      base: "/training_center/carmen_onpermise/CADENA/ca-",
      items: [
        {
          text: "Time Attandance",
          collapsed: true,
          items: [
            {
              text: "TA Data Setup",
              link: "index1",
            },

            {
              text: "TA Holiday Data Setup",
              link: "index2",
            },
          ],
        },
        {
          text: "Staffing",
          collapsed: true,
          items: [
            {
              text: "Transaction",
              link: "index3",
            },
            {
              text: "Staffing Data Setup",
              link: "index4",
            },
            {
              text: "Resignation",
              link: "index5",
            },
            {
              text: "Employee Profile",
              link: "index6",
            },
            {
              text: "Add New Employee",
              link: "index7",
            },
          ],
        },
        {
          text: "System Setting",
          collapsed: true,
          items: [
            {
              text: "Workflow Management",
              link: "index8",
            },
            {
              text: "Security",
              link: "index9",
            },
            {
              text: "Import",
              link: "index10",
            },
            {
              text: "General Settings",
              link: "index11",
            },
            {
              text: "Email Management",
              link: "index12",
            },
          ],
        },
        {
          text: "Leave Management",
          collapsed: true,
          items: [
            {
              text: "Leave Data Setup",
              link: "index13",
            },
          ],
        },
      ],
    },
  ];
}
function sidebarBL() {
  return [
    {
      text: "Procurement",
      collapsed: true,
      base: "/Blueledgers/Procurement/P-",
      items: [
        { text: "Purchase Request", link: "Purchase Request" },
        { text: "Purchase Order", link: "Purchase Order" },
        { text: "Receiving", link: "Receiving" },
        { text: "Credit Note", link: "Credit Note" },
        { text: "Product", link: "Product" },
        {
          text: "Configuration",
          collapsed: true,
          items: [
            {
              text: "Price List",
              link: "Price List",
            },
            {
              text: "Extra Cost",
              link: "Extra Cost",
            },
            {
              text: "Market List",
              link: "Market List",
            },
            {
              text: "Standard Order",
              link: "Standardorder",
            },
            {
              text: "Account Code Mapping",
              link: "Account Code Mapping",
            },
            {
              text: "Movement Type Definition",
              link: "Movement Type",
            },
            {
              text: "Currency",
              link: "Currency",
            },
            {
              text: "Exchange Rate",
              link: "Exchange Rate",
            },
            {
              text: "Delivery Point",
              link: "Delivery Point",
            },
            {
              text: "Unit",
              link: "Unit",
            },
            {
              text: "Category",
              link: "Category",
            },
            {
              text: "Store/Location",
              link: "StoreLocation",
            },
          ],
        },
      ],
    },
    {
      text: "Material",
      collapsed: true,
      base: "/Blueledgers/Material/M-",
      items: [
        { text: "Store Requisition", link: "Store Requisition" },
        { text: "Stock In", link: "Stock In" },
        { text: "Stock Out", link: "Stock Out" },
        {
          text: "Procedure",
          collapsed: true,
          items: [
            {
              text: "Closing Balance",
              link: "Closing Balance",
            },
            {
              text: "Period End",
              link: "Period End",
            },
          ],
        },
        { text: "Product Restock", link: "Product Restock" },
        {
          text: "Configuration",
          collapsed: true,
          items: [
            {
              text: "Adjustment Type",
              link: "Adjustment Type",
            },
            {
              text: "Standard Requisition",
              link: "Standard Requisition",
            },
          ],
        },
      ],
    },
    {
      text: "Portions",
      collapsed: true,
      base: "/Blueledgers/Portions/O-",
      items: [
        { text: "Recipe", link: "Recipe" },
        { text: "Category", link: "Category" },
        { text: "Sale", link: "Sale" },
      ],
    },
    {
      text: "Options",
      collapsed: true,
      base: "/Blueledgers/Options/op-",
      items: [
        { text: "Personal Setting", link: "Personal Setting" },
        {
          text: "Administrator",
          collapsed: true,
          items: [
            {
              text: "Role",
              link: "Role",
            },
            {
              text: "User",
              link: "User",
            },
            {
              text: "Department",
              link: "Department",
            },
            {
              text: "Work-flow Configuration",
              link: "Work-flow Configuration",
            },
          ],
        },
        { text: "System Setting", link: "System Setting" },
      ],
    },
  ];
}
