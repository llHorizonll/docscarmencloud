import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "TRAINING CENTER",
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
            text: "🆕 January2025 Relaese Infomation",
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
      '/': { base: '/carmen_cloud/', items: sidebarAll() },
      '/training_center/': { base: '/training_center/', items: sidebarTraining() }
    },
    

    socialLinks: [{ icon: "github", link: "https://github.com/llHorizonll/docscarmencloud" }],
    search: {
      provider: "local",
    },
  },
});

function sidebarAll() {
  return [
    {
      text: "Dashboard",
      link: "/dashboard/",
    },
    {
      text: "General Ledger",
      collapsed: true,
      items: [
        { text: "Journal Voucher", link: "carmen_cloud/gl/journal_voucher" },
        { text: "Template Voucher", link: "carmen_cloud/gl/template_voucher" },
        { text: "Recurring Voucher", link: "carmen_cloud/gl/recurring_voucher" },
        { text: "Amortization Voucher", link: "carmen_cloud/gl/amortization_voucher" },
        { text: "Allocation Voucher", link: "carmen_cloud/gl/allocation_voucher" },
        { text: "Budget", link: "carmen_cloud/gl/budget" },
        { text: "Posting Account Payable to GL", link: "carmen_cloud/gl/posting_ap" },
        { text: "Posting Account Receivable to GL", link: "carmen_cloud/gl/posting_ar" },
        { text: "Inventory & Extra Cost Posting to GL", link: "carmen_cloud/gl/posting_inventory" },
        { text: "Posting Fixed Assets to GL", link: "carmen_cloud/gl/posting_asset" },
        { text: "Close Period and Year End", link: "carmen_cloud/gl/close_period" },
      ],
    },
    {
      text: "Account Payable",
      collapsed: true,
      items: [
        { text: "Vendor", link: "carmen_cloud/ap/vendor" },
        { text: "Posting AP invoice from recieving", link: "carmen_cloud/ap/recevingToAp" },
        { text: "Invoice", link: "carmen_cloud/ap/invoice" },
        { text: "Payment", link: "carmen_cloud/ap/payment" },
        { text: "Deposit Payment", link: "carmen_cloud/ap/deposit_payment" },
        { text: "Apply Deposit with Invoice", link: "carmen_cloud/ap/apply_deposit_pay_with_inv" },
        { text: "Cheque Reconciliation", link: "carmen_cloud/ap/cheque_reconciliation" },
        { text: "Input Tax Reconciliation", link: "carmen_cloud/ap/input_tax_reconciliation" },
        { text: "WHT Reconciliation", link: "carmen_cloud/ap/wht_reconciliation" },
        { text: "RDPrep_การโอนย้ายข้อมูลใบแนบ ภงด 3", link: "carmen_cloud/ap/RDPrep_3" },
        { text: "RDPrep_การโอนย้ายข้อมูลใบแนบ ภงด 53", link: "carmen_cloud/ap/RDPrep_53" },
        { text: "Close Period AP", link: "carmen_cloud/ap/close_period" },
      ],
    },
    {
      text: "Account Receivable",
      collapsed: true,
      items: [
        { text: "Profile", link: "carmen_cloud/ar/profile" },
        { text: "AR Posting from PMS (PMS Interface)", link: "carmen_cloud/ar/posting_pms" },
        { text: "Folio", link: "carmen_cloud/ar/folio" },
        { text: "Invoice", link: "carmen_cloud/ar/invoice" },
        { text: "Contract", link: "carmen_cloud/ar/contract" },
        { text: "Apply AR Contract", link: "carmen_cloud/ar/apply_contract" },
        { text: "Receipt", link: "carmen_cloud/ar/receipt" },
        { text: "Receipt for Advance Deposit", link: "carmen_cloud/ar/receipt_advance_deposit" },
        { text: "Apply invoice for Advance Deposit", link: "carmen_cloud/ar/apply_invoice_advance_deposit" },
        { text: "Close Period AR", link: "carmen_cloud/ar/close_period" },
      ],
    },
    {
      text: "Asset",
      collapsed: true,
      items: [
        { text: "Pre-Register Asset Setting", link: "carmen_cloud/asset/preasset_setting" },
        { text: "Pre-Register Asset", link: "carmen_cloud/asset/preasset" },
        { text: "Asset Register", link: "carmen_cloud/asset/asset_register" },
        { text: "Print Asset QR Code", link: "carmen_cloud/asset/print_asset" },
        { text: "Asset Disposal", link: "carmen_cloud/asset/asset_disposal" },
        { text: "Asset Checker", link: "carmen_cloud/asset/asset_checker" },
        { text: "Close Period Asset", link: "carmen_cloud/asset/close_period" },
      ],
    },
    {
      text: "Comment and Document Management & Activity Log",
      link: "/comment/",
    },
    {
      text: "Work Book",
      collapsed: true,
      items: [
        { text: "Installation and Configuration", link: "carmen_cloud/workbook/install&config" },
        { text: "Work Book Function", link: "carmen_cloud/workbook/function" },
      ],
    },
    {
      text: "Configuration",
      collapsed: true,
      items: [
        { text: "Product License", link: "carmen_cloud/configuration/product_license" },
        { text: "Company Profile", link: "carmen_cloud/configuration/company_profile" },
        { text: "System Preference", link: "carmen_cloud/configuration/system_preference" },
        { text: "Users", link: "carmen_cloud/configuration/users" },
        { text: "Change Password User", link: "carmen_cloud/configuration/change_password_user" },
        { text: "Permissions", link: "carmen_cloud/configuration/permissions" },
        { text: "Currency Exchange Rate", link: "carmen_cloud/configuration/currency_exrate" },
        { text: "Currency", link: "carmen_cloud/configuration/currency" },
        { text: "Department", link: "carmen_cloud/configuration/department" },
        { text: "Chart Of Accounts", link: "carmen_cloud/configuration/chart_of_account" },
        { text: "Payment Type", link: "carmen_cloud/configuration/payment_type" },
        { text: "Dimension", link: "carmen_cloud/configuration/dimension" },
        { text: "Unit", link: "carmen_cloud/configuration/unit" },
      ],
    },
    {
      text: "TRAINING CENTER",
      link: "/training_center/",
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
          text: "AP",
          collapsed: true,
          items: [],
        },

        {
          text: "AR",
          collapsed: true,
          items: [],
        },
        {
          text: "GL",
          collapsed: true,
          items: [],
        },
      ],
    },
    {
      text: "Carmen On-Permise",
      collapsed: false,
      items: [
        {
          text: "AP",
          collapsed: true,
          items: [
            {
              text: "on-permise AP",
              link: "/carmen-on-permise/AP",
            },
          ],
        },
        {
          text: "AR",
          collapsed: true,
          items: [
            {
              text: "on-permise AR",
              link: "/carmen-on-permise/AR",
            },
          ],
        },
        {
          text: "GL",
          collapsed: true,
          items: [
            {
              text: "on-permise GL",
              link: "/carmen-on-permise/GL",
            },
          ],
        },
      ],
    },
    {
      text: "Cadena",
      collapsed: false,
      items: [],
    },
  ];
}
