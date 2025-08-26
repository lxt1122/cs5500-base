#!/usr/bin/env python3

import os
import argparse

def create_retrospective_documents():
    """
    Create retrospective documents for each week starting from September 14th
    """
    
    # Array of week numbers and dates for retrospectives
    weeks = [
        "Week 1 September 14",
        "Week 2 September 21",
        "Week 3 September 28",
        "Week 4 October 05",
        "Week 5 October 12",
        "Week 6 October 19",
        "Week 7 October 26",
        "Week 8 November 02",
        "Week 9 November 09",
        "Week 10 November 16",
        "Week 11 November 23",
    ]
    
    # Template content for retrospective documents
    retrospective_template = """# Retrospective Document Template

## Team Name
[Insert Team Name Here]

## Date
{date}

## Participants
- [Team Member 1]
- [Team Member 2]
- [Team Member 3]
- [Team Member 4]
- [Team Member 5]

---

## Overview
Briefly describe the purpose of this retrospective and what you aim to achieve.

---

## What Went Well
List the things that went well during the project.
-
-
-

---

## What Could Be Improved
List the areas where there is room for improvement.
-
-
-

---

## Action Items
Identify actionable steps that can be taken to improve future projects.
1.
2.
3.

---

## Individual Self-Assessments
### [Team Member 1]
- **Achievements and Contributions:**
  -
- **Challenges Faced:**
  -
- **Areas for Improvement:**
  -
- **Feedback and Suggestions:**
  -

### [Team Member 2]
- **Achievements and Contributions:**
  -
- **Challenges Faced:**
  -
- **Areas for Improvement:**
  -
- **Feedback and Suggestions:**
  -

### [Team Member 3]
- **Achievements and Contributions:**
  -
- **Challenges Faced:**
  -
- **Areas for Improvement:**
  -
- **Feedback and Suggestions:**
  -

### [Team Member 4]
- **Achievements and Contributions:**
  -
- **Challenges Faced:**
  -
- **Areas for Improvement:**
  -
- **Feedback and Suggestions:**
  -

### [Team Member 5]
- **Achievements and Contributions:**
  -
- **Challenges Faced:**
  -
- **Areas for Improvement:**
  -
- **Feedback and Suggestions:**
  -

---

## Overall Team Assessment
Reflect on the team's performance as a whole.
- **Team Strengths:**
  -
- **Areas for Improvement:**
  -
- **Suggestions for Future Projects:**
  -

---

## Additional Comments
Add any additional comments or notes that may be relevant.
-
"""
    
    created_files = []
    
    # Create each retrospective document
    for week in weeks:
        # Create filename by replacing spaces with hyphens
        retro_filename = f"{week.replace(' ', '-')}-retrospective.md"
        
        try:
            with open(retro_filename, 'w') as file:
                file.write(retrospective_template.format(date=week))
            print(f"Created: {retro_filename}")
            created_files.append(retro_filename)
        except IOError as e:
            print(f"Error creating {retro_filename}: {e}")
            return False, []
    
    return True, created_files

def create_sharing_documents():
    """
    Create knowledge sharing documents for each week starting from September 15th
    """
    
    # Dictionary of dates with student presentation flag and project titles
    sharing_schedule = {
        "Week-02-September-15": {"student": True, "title": None},
        "Week-03-September-22": {"student": False, "title": "Project Kickoff"},
        "Week-04-September-29": {"student": True, "title": None},
        "Week-05-October-06": {"student": True, "title": None},
        "Week-06-October-13": {"student": True, "title": None},
        "Week-07-October-20": {"student": False, "title": "Project Pitch"},
        "Week-08-October-27": {"student": True, "title": None},
        "Week-09-November-03": {"student": True, "title": None},
        "Week-10-November-10": {"student": False, "title": "Research Paper Presentations"},
        "Week-11-November-17": {"student": False, "title": "Play Test"},
        "Week-12-November-24": {"student": False, "title": "MVP Demo"},
        "Week-13-December-01": {"student": True, "title": None},
        "Week-14-December-08": {"student": False, "title": "Final Project Presentations"},
    }
    
    # Template content for student sharing documents
    student_sharing_template = """# Knowledge Sharing Document

## Sharer Name
_____________________________

## Topic
_____________________________

## Main Lessons Learned

### Key Takeaways
- 
- 
- 

### Technical Insights
- 
- 
- 

### Best Practices
- 
- 
- 

### Challenges and Solutions
- 
- 
- 

### Resources and References
- 
- 
- 
"""

    # Template content for project milestone documents
    project_milestone_template = """# Project Milestone Document

## Session Title
{title}

## Date
{date}

## Facilitator/Presenter
_____________________________

## Agenda

### Objectives
- 
- 
- 

### Key Discussion Points
- 
- 
- 

### Demonstrations/Presentations
- 
- 
- 

## Outcomes and Decisions

### Key Decisions Made
- 
- 
- 

### Action Items
1. 
2. 
3. 

### Next Steps
- 
- 
- 

## Feedback and Notes

### Positive Feedback
- 
- 
- 

### Areas for Improvement
- 
- 
- 

### Additional Comments
- 
- 
- 
"""
    
    created_files = []
    
    # Create each sharing document based on type
    for date, info in sharing_schedule.items():
        if info["student"]:
            # Student presentation
            share_filename = f"{date}-share.md"
            template_content = student_sharing_template
            doc_type = "student sharing"
        else:
            # Project milestone
            share_filename = f"{date}-milestone.md"
            # Extract readable date from the date key (e.g., "Week-02-September-15" -> "Week 2 September 15")
            readable_date = date.replace("-", " ").replace("Week ", "Week ")
            template_content = project_milestone_template.format(
                title=info["title"], 
                date=readable_date
            )
            doc_type = "project milestone"
        
        try:
            with open(share_filename, 'w') as file:
                file.write(template_content)
            print(f"Created: {share_filename} ({doc_type})")
            created_files.append(share_filename)
        except IOError as e:
            print(f"Error creating {share_filename}: {e}")
            return False, []
    
    return True, created_files

def main():
    """
    Main function to handle command line arguments and create documents
    """
    parser = argparse.ArgumentParser(description='Create retrospective and/or sharing documents')
    parser.add_argument('--retrospectives', '-r', action='store_true', 
                       help='Create retrospective documents')
    parser.add_argument('--sharing', '-s', action='store_true', 
                       help='Create knowledge sharing documents')
    parser.add_argument('--all', '-a', action='store_true', 
                       help='Create both retrospective and sharing documents')
    
    args = parser.parse_args()
    
    # If no specific arguments, create all documents
    if not (args.retrospectives or args.sharing or args.all):
        args.all = True
    
    total_created = 0
    
    if args.retrospectives or args.all:
        print("Creating retrospective documents...")
        success, files = create_retrospective_documents()
        if success:
            total_created += len(files)
            print(f"Successfully created {len(files)} retrospective documents.")
        else:
            print("Failed to create retrospective documents.")
            return 1
    
    if args.sharing or args.all:
        print("\nCreating knowledge sharing documents...")
        success, files = create_sharing_documents()
        if success:
            total_created += len(files)
            print(f"Successfully created {len(files)} sharing documents.")
        else:
            print("Failed to create sharing documents.")
            return 1
    
    print(f"\nTotal documents created: {total_created}")
    print("All documents created successfully!")
    return 0

if __name__ == "__main__":
    exit(main())
