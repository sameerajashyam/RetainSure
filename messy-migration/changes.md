# CHANGES.md

##Major Issues in Original Code

1. Poor Code Organization
   - All application logic, route handling, and database operations were bundled inside a single app.py.
   - This made the code hard to understand, test, or maintain.

2. Security Flaws
   - Passwords were stored in plaintext a major security vulnerability.
   - No hashing, salting, or encryption was used.
   - Login had no validation or protection against malicious inputs.

3. Lack of Error Handling
   - Errors were not handled gracefully.
   - There was no consistent use of HTTP status codes or response formatting

4. Scalability & Developer Experience Issues
   - No modularity.
   - Difficult to understand
   - Not production-ready


##  Changes Made

1. Refactored Project Structure
   - Introduced a modular folder layout:
     - routes: All API route logic
     - models: Database query operations
     - utils: Reusable helpers  password hashing
     - db/: Centralized database connection db.py
   - Used Flask Blueprints for modular, scalable route registration.

2. Security Improvements
   - Implemented password hashing using werkzeug.security.
   - Replaced all raw SQL interpolation with parameterized queries to prevent SQL injection.
   - Improved login logic with secure password validation.

3. Best Practices & Maintainability
   - Added structured and consistent JSON responses.
   - Proper use of HTTP status codes (200, 400, 401, 404, 500).
   - Simplified future testing by separating logic from routing.

---

##  AI Usage Disclosure

- Tool Used: ChatGPT 
- Used For:
  - Designing a clean, modular Flask codebase
  -  secure password storage practices
