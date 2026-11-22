"""
================================================================================
Sindh Madressatul Islam University (SMIU)
Department of Cyber Security (BSCY) - 4th Semester
Project: Library Management System
Group Members:
  1. Huzaifa Shoukat Ali  (BCB-25S-044)
  2. Husnain Nawaz         (BCB-25S-017)
  3. Sualeh Talal          (BCB-25S-040)
================================================================================
"""

import sys

class LibraryManagementSystem:
    def __init__(self):
        # Database structure: {book_id: {"title": str, "author": str, "issued": bool}}
        self.books = {
            "101": {
                "title": "Computer Organization & Architecture",
                "author": "William Stallings",
                "issued": False
            },
            "102": {
                "title": "Assembly Language for x86 Processors",
                "author": "Kip Irvine",
                "issued": False
            },
            "103": {
                "title": "Operating System Concepts",
                "author": "Abraham Silberschatz",
                "issued": True
            },
            "104": {
                "title": "Introduction to Computer Security",
                "author": "Matt Bishop",
                "issued": False
            }
        }

    def display_menu(self):
        print("\n" + "=" * 52)
        print("    SMIU LIBRARY MANAGEMENT SYSTEM - CONSOLE CLI")
        print("=" * 52)
        print("  [1] View Complete Book Catalog")
        print("  [2] Add New Book Record")
        print("  [3] Search Book by ID or Title")
        print("  [4] Issue a Book (Checkout)")
        print("  [5] Return a Book (Check-in)")
        print("  [6] Terminate System")
        print("=" * 52)

    def view_books(self):
        print("\n" + "-" * 88)
        print("                         CURRENT LIBRARY INVENTORY")
        print("-" * 88)
        if not self.books:
            print("  Notice: Inventory is empty. No records available.")
            return

        print(f"  {'Book ID':<9} | {'Title':<42} | {'Author':<22} | {'Status':<10}")
        print("  " + "-" * 84)

        for b_id, details in self.books.items():
            status = "Issued" if details["issued"] else "Available"
            print(f"  {b_id:<9} | {details['title']:<42} | {details['author']:<22} | {status:<10}")
        print("-" * 88)

    def add_book(self):
        print("\n>>> MODULE: ADD NEW BOOK RECORD")
        b_id = input("  Enter Unique Book ID (e.g., 105): ").strip()
        
        # Validation 1: Empty input check
        if not b_id:
            print("  [!] Error: Book ID cannot be empty.")
            return

        # Validation 2: Duplicate key collision check
        if b_id in self.books:
            print(f"  [!] Error: Record with ID '{b_id}' already exists in database.")
            return

        title = input("  Enter Book Title: ").strip()
        author = input("  Enter Author Name: ").strip()

        # Validation 3: Field completeness check
        if not title or not author:
            print("  [!] Error: Title and Author fields cannot be blank.")
            return

        # Commit to memory store
        self.books[b_id] = {
            "title": title,
            "author": author,
            "issued": False
        }
        print(f"  [+] Success: Book '{title}' (ID: {b_id}) successfully registered in inventory.")

    def search_book(self):
        print("\n>>> MODULE: SEARCH INVENTORY")
        query = input("  Enter Book ID or Title keyword: ").strip().lower()
        if not query:
            print("  [!] Error: Search term cannot be empty.")
            return

        found_records = []
        for b_id, details in self.books.items():
            if query == b_id.lower() or query in details["title"].lower():
                found_records.append((b_id, details))

        if not found_records:
            print(f"  [-] Result: No records matching query '{query}' were found.")
            return

        print(f"\n  Found {len(found_records)} matching record(s):")
        print("  " + "-" * 80)
        for b_id, details in found_records:
            status = "Issued" if details["issued"] else "Available"
            print(f"  * ID:      {b_id}")
            print(f"    Title:   {details['title']}")
            print(f"    Author:  {details['author']}")
            print(f"    Status:  {status}")
            print("  " + "-" * 80)

    def issue_book(self):
        print("\n>>> MODULE: ISSUE BOOK (CHECKOUT)")
        b_id = input("  Enter Book ID to issue: ").strip()

        if b_id not in self.books:
            print(f"  [!] Error: Book ID '{b_id}' does not exist in inventory.")
            return

        # State check: Cannot issue a book that is already checked out
        if self.books[b_id]["issued"]:
            print(f"  [!] Warning: '{self.books[b_id]['title']}' is currently marked as ISSUED.")
            print("      Cannot perform checkout until the item is returned.")
        else:
            self.books[b_id]["issued"] = True
            print(f"  [+] Transaction Approved: '{self.books[b_id]['title']}' marked as ISSUED.")

    def return_book(self):
        print("\n>>> MODULE: RETURN BOOK (CHECK-IN)")
        b_id = input("  Enter Book ID to return: ").strip()

        if b_id not in self.books:
            print(f"  [!] Error: Book ID '{b_id}' does not exist in inventory.")
            return

        # State check: Cannot return a book that is already marked available
        if not self.books[b_id]["issued"]:
            print(f"  [!] Notice: '{self.books[b_id]['title']}' is already marked as AVAILABLE.")
            print("      No outstanding checkout found for this record.")
        else:
            self.books[b_id]["issued"] = False
            print(f"  [+] Return Accepted: '{self.books[b_id]['title']}' marked as AVAILABLE.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("  Enter choice [1-6]: ").strip()

            if choice == "1":
                self.view_books()
            elif choice == "2":
                self.add_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.issue_book()
            elif choice == "5":
                self.return_book()
            elif choice == "6":
                print("\n  Terminating Library Management System session.")
                print("  Developed by Huzaifa, Husnain, and Sualeh. Goodbye!\n")
                sys.exit(0)
            else:
                print("  [!] Invalid selection. Please enter a numerical option from 1 to 6.")

if __name__ == "__main__":
    app = LibraryManagementSystem()
    app.run()