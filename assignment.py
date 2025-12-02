from fpdf import FPDF

class ChurchAssignmentPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'Church Project: Full Stack Integration', 0, 1, 'R')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def section_title(self, label):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(75, 0, 130) # Indigo/Purple (React/Web vibe)
        self.cell(0, 10, label, 0, 1, 'L')
        self.set_draw_color(75, 0, 130)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def sub_title(self, label):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 0, 0)
        self.cell(0, 8, label, 0, 1, 'L')
        self.ln(2)

    def body_text(self, text):
        self.set_font('Arial', '', 11)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 6, text)
        self.ln(3)

    # Green box for friendly tips
    def friendly_tip(self, text):
        self.set_font('Arial', 'I', 10)
        self.set_text_color(0, 100, 0) # Dark Green
        self.set_fill_color(235, 250, 235) # Very Light Green
        self.multi_cell(0, 6, f"TIP: {text}", 0, 'L', True)
        self.set_text_color(0, 0, 0) # Reset
        self.ln(4)

    def code_block(self, code):
        self.set_font('Courier', '', 9)
        self.set_fill_color(245, 245, 245) # Light Grey
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 5, code, 0, 'L', True)
        self.ln(4)

    def checklist_item(self, text):
        self.set_font('Courier', 'B', 12)
        self.cell(8, 6, '[ ]', 0, 0)
        self.set_font('Arial', '', 11)
        self.cell(0, 6, text, 0, 1)

    def endpoint_row(self, resource, url, desc):
        self.set_font('Courier', 'B', 10)
        self.cell(40, 8, resource, 1)
        self.set_font('Courier', '', 9)
        self.cell(60, 8, url, 1)
        self.set_font('Arial', '', 10)
        self.cell(0, 8, desc, 1, 1)

pdf = ChurchAssignmentPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# ==========================================
# PAGE 1: OBJECTIVE & BACKEND
# ==========================================
pdf.add_page()
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 10, 'Full-Stack Assignment: Church Project', 0, 1, 'C')
pdf.set_font('Arial', 'I', 12)
pdf.cell(0, 8, 'React Integration with Django', 0, 1, 'C')
pdf.ln(8)

pdf.section_title("1. Project Goal")
pdf.body_text("You will build a React frontend that interacts with your existing Django church APIs. You will create components to fetch, display, add, update, and delete data for sermons, events, ministries, and more.")

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, "Deadline: Friday, 26th December 2025", 0, 1)
pdf.ln(5)

pdf.section_title("2. Technical Requirements: Backend")
pdf.body_text("You already have these endpoints. Ensure they are running and returning JSON:")

# Endpoint Table
pdf.set_fill_color(230, 230, 250) # Light Lavender
pdf.set_font('Arial', 'B', 10)
pdf.cell(40, 8, "Resource", 1, 0, 'C', True)
pdf.cell(60, 8, "Endpoint", 1, 0, 'C', True)
pdf.cell(0, 8, "Description", 1, 1, 'C', True)

pdf.endpoint_row("Sermons", "/api/sermons/", "List & CRUD Sermons")
pdf.endpoint_row("Events", "/api/events/", "List & CRUD Events")
pdf.endpoint_row("Ministries", "/api/ministries/", "List & CRUD Ministries")
pdf.endpoint_row("Homepage", "/api/homepage/", "Homepage Content")
pdf.endpoint_row("Livestreams", "/api/livestreams/", "Livestream Sessions")
pdf.ln(5)

pdf.friendly_tip("Test all these in Postman first! If the backend doesn't work, the frontend won't work.")

# ==========================================
# PAGE 2: FRONTEND & CODE EXAMPLE
# ==========================================
pdf.add_page()
pdf.section_title("3. Technical Requirements: Frontend")
pdf.body_text("1. Create a React app: `npx create-react-app church-frontend`\n2. Install Axios: `npm install axios`\n3. Build reusable components for each resource above.")

pdf.sub_title("Example Component: SermonList.js")
pdf.body_text("Use this pattern to Fetch and Delete data. You can adapt this for Events and Ministries.")

pdf.code_block("""import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SermonList = () => {
  const [sermons, setSermons] = useState([]);

  useEffect(() => {
    fetchSermons();
  }, []);

  const fetchSermons = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/sermons/');
      setSermons(response.data);
    } catch (error) {
      console.error('Error fetching sermons:', error);
    }
  };

  const deleteSermon = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/api/sermons/${id}/`);
      fetchSermons(); // Refresh the list after deleting
    } catch (error) {
      console.error('Error deleting sermon:', error);
    }
  };

  return (
    <div>
      <h2>Sermons</h2>
      <ul>
        {sermons.map(s => (
          <li key={s.id}>
            {s.title} - {s.date}
            <button onClick={() => deleteSermon(s.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SermonList;""")

# ==========================================
# PAGE 3: STEPS & SUBMISSION
# ==========================================
pdf.add_page()
pdf.section_title("4. Step-by-Step Instructions")

pdf.sub_title("Phase 1: Setup")
pdf.checklist_item("Test backend endpoints in Postman.")
pdf.checklist_item("Create React App & install Axios.")

pdf.sub_title("Phase 2: Development")
pdf.checklist_item("Build SermonList (Fetch & Display).")
pdf.checklist_item("Add Delete button to Sermons.")
pdf.checklist_item("Create 'AddSermon' form (Create).")
pdf.checklist_item("Repeat for Events, Ministries, etc.")

pdf.sub_title("Phase 3: Polish")
pdf.checklist_item("Add simple validation (e.g., Title required).")
pdf.checklist_item("Clean up CSS/Styling.")

pdf.ln(5)
pdf.section_title("5. Submission Requirements")
pdf.body_text("Please submit the following by the deadline:")

pdf.checklist_item("GitHub Repository (Frontend + Backend folders).")
pdf.checklist_item("Demo Video (3-5 mins) showing CRUD operations.")
pdf.checklist_item("README.md explaining how to run the project.")

pdf.ln(5)
pdf.friendly_tip("Take it one resource at a time. Start with Sermons. Once that works, the rest is just copy-paste-modify! You are building a real full-stack app!")

pdf.output("Church_FullStack_Assignment.pdf")
print("PDF generated successfully: Church_FullStack_Assignment.pdf")