events = [
    "Login",
    "Logout",
    "ViewHome",
    "ViewAccounts",
    "ViewProducts",
    "SelectTransfer",
    "ViewTransactions",
    "ViewCreditCard",
    "ViewLoan",
    "ApplyCreditCard",
    "ApplyLoan",
    "FillCreditCardApplication",
    "FillLoanApplication",
    "SubmitCreditCardApplication",
    "SubmitLoanApplication",
    "FillTransferDetails",
    "CompleteTransfer"
]

weighted_events = [
    {
        "name": "Login",
        "popularity": 0,
        "dependsOn": [],
        "dependencyFilter": "any"
    },
    {
        "name": "Logout",
        "popularity": 30,
        "dependsOn": ["Login"],
        "dependencyFilter": "any"
    },
    {
        "name": "ViewHome",
        "popularity": 90,
        "dependsOn": ["Login"],
        "dependencyFilter": "any"
    },
    {
        "name": "ViewAccounts",
        "popularity": 60,
        "dependsOn": ["Login"],
        "dependencyFilter": "any"
    },
    {
        "name": "ViewProducts",
        "popularity": 30,
        "dependsOn": ["Login"],
        "dependencyFilter": "any"
    },
    {
        "name": "SelectTransfer",
        "popularity": 40,
        "dependsOn": ["Login"],
        "dependencyFilter": "any"
    },
    {
        "name": "ViewTransactions",
        "popularity": 40,
        "dependsOn": ["ViewAccounts"],
        "dependencyFilter": "any"
    },
    {
        "name": "ViewCreditCard",
        "popularity": 25,
        "dependsOn": ["ViewProducts"],
        "dependencyFilter": "any"
    },
    {
        "name": "ViewLoan",
        "popularity": 15,
        "dependsOn": ["ViewProducts"],
        "dependencyFilter": "any"
    },
    {
        "name": "ApplyCreditCard",
        "popularity": 15,
        "dependsOn": ["ViewProducts"],
        "dependencyFilter": "any"
    },
    {
        "name": "ApplyLoan",
        "popularity": 10,
        "dependsOn": ["ViewProducts"],
        "dependencyFilter": "any"
    },
    {
        "name": "FillCreditCardApplication",
        "popularity": 12,
        "dependsOn": ["ApplyCreditCard"],
        "dependencyFilter": "any"
    },
    {
        "name": "FillLoanApplication",
        "popularity": 8,
        "dependsOn": ["ApplyLoan"],
        "dependencyFilter": "any"
    },
    {
        "name": "SubmitCreditCardApplication",
        "popularity": 11,
        "dependsOn": ["ApplyCreditCard"],
        "dependencyFilter": "any"
    },
    {
        "name": "SubmitLoanApplication",
        "popularity": 7,
        "dependsOn": ["ApplyLoan"],
        "dependencyFilter": "any"
    },
    {
        "name": "FillTransferDetails",
        "popularity": 35,
        "dependsOn": ["SelectTransfer"],
        "dependencyFilter": "any"
    },
    {
        "name": "CompleteTransfer",
        "popularity": 30,
        "dependsOn": ["FillTransferDetails"],
        "dependencyFilter": "any"
    }
]