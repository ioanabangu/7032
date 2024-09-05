<strong> GardenGuard: Secure Customer Management System </strong>

<strong>Project Overview</strong>

GardenGuard is a web-based application designed for a gardening business to securely manage customer data and service bookings. The system allows authorized staff to log in, view, add, update, and remove customer information, ensuring that sensitive data such as addresses and phone numbers are protected in compliance with legal regulations like GDPR.

<strong>Features</strong>

<ul>
<li><strong>User Authentication</strong>: Staff can log in securely with password hashing.</li>
<li><strong>Customer Management</strong>: View, add, edit, and delete customer records, including booking details and preferences.</li>
<li><strong>Data Security</strong>: Customer data is stored securely in a MySQL database, with access limited to authorized users.</li>
<li><strong>Role-based Access</strong>: Each staff member can only access their own clients.</li>
</ul>

<strong>Technologies Used</strong>

<ul>
<li><strong>Backend</strong>: Python Flask</li>
<li><strong>Frontend</strong>: HTML, Bootstrap</li>
<li><strong>Database</strong>: MySQL</li>
<li><strong>Security</strong>: Password hashing for user authentication</li>
</ul>

<strong>Getting Started</strong>
<strong>Prerequisites</strong>
<ul>
<li>Python 3.x </li>
<li>Flask</li>
<li>MySQL</li>
<li>Bootstrap</li>
</ul>

<strong>Installation</strong>
<ol>
  <li>Clone the repository</li>
  <li>Install the required Python packages</li>
  <li>Create a MySQL database and update the config.py file with your database credentials.
Import the provided SQL scripts to create the necessary tables.</li>
   <li>Access the website</li>
</ol>

<strong>Usage</strong>
<ol>
  <li><strong>Sign Up/Login</strong>: Staff can create accounts and log in.</li>
   <li><strong>Customer Management</strong>: After logging in, staff can view, add, edit, and delete customer records.</li>
    <li><strong>Security</strong>: All passwords are hashed before being stored in the database.</li>
</ol>


<strong>Legal Considerations</strong>
The system is designed to comply with GDPR regulations, ensuring the secure storage and handling of customer data.

<strong>Future Enhancements</strong>
<ul>
<li>Mobile compatibility for easy access on smartphones.</li>
  <li>Admin-created user accounts for added security.</li>
  <li>Additional security testing and user access control improvements.</li>
</ul>
