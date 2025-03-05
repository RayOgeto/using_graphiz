from graphviz import Digraph

def generate_level_0():
    """Creates Level 0 DFD (Context Diagram)"""
    dfd0 = Digraph("Level_0_DFD", format="jpg")

    # External Entities
    dfd0.node("Employees", shape="rectangle", style="filled", fillcolor="lightblue")
    dfd0.node("HR", label="Human Resources", shape="rectangle", style="filled", fillcolor="lightblue")
    dfd0.node("KRA", label="Kenya Revenue Authority", shape="rectangle", style="filled", fillcolor="lightblue")
    dfd0.node("Management", shape="rectangle", style="filled", fillcolor="lightblue")

    # Main System
    dfd0.node("Payroll System", shape="ellipse", style="filled", fillcolor="lightgreen")

    # Connections
    dfd0.edge("Employees", "Payroll System", label="Time Data")
    dfd0.edge("HR", "Payroll System", label="Personnel Changes")
    dfd0.edge("Payroll System", "Employees", label="Paychecks")
    dfd0.edge("Payroll System", "KRA", label="Tax Reports")
    dfd0.edge("Payroll System", "Management", label="Payroll Reports")

    # Render
    dfd0.render("level_0_dfd_payroll", format="jpg", cleanup=True)

def generate_level_1():
    """Creates Level 1 DFD (Breakdown of Payroll Processing System)"""
    dfd1 = Digraph("Level_1_DFD", format="jpg")

    # External Entities
    dfd1.node("Employees", shape="rectangle", style="filled", fillcolor="lightblue")
    dfd1.node("HR", label="Human Resources", shape="rectangle", style="filled", fillcolor="lightblue")
    dfd1.node("KRA", label="Kenya Revenue Authority", shape="rectangle", style="filled", fillcolor="lightblue")
    dfd1.node("Management", shape="rectangle", style="filled", fillcolor="lightblue")

    # Processes
    dfd1.node("P1", "Collect & Record Time Data", shape="ellipse", style="filled", fillcolor="lightgreen")
    dfd1.node("P2", "Enter Payroll & HR Data", shape="ellipse", style="filled", fillcolor="lightgreen")
    dfd1.node("P3", "Process Payroll & Generate Paychecks", shape="ellipse", style="filled", fillcolor="lightgreen")
    dfd1.node("P4", "Generate Payroll & Tax Reports", shape="ellipse", style="filled", fillcolor="lightgreen")

    # Data Stores
    dfd1.node("D1", "Payroll File", shape="cylinder", style="filled", fillcolor="lightgrey")
    dfd1.node("D2", "Employee Records", shape="cylinder", style="filled", fillcolor="lightgrey")
    dfd1.node("D3", "Payroll Reports", shape="cylinder", style="filled", fillcolor="lightgrey")

    # Connections
    dfd1.edge("Employees", "P1", label="Time Data")
    dfd1.edge("HR", "P2", label="Personnel Changes")

    dfd1.edge("P1", "D1", label="Store Time Data")
    dfd1.edge("P2", "D1", label="Update Payroll File")
    dfd1.edge("P3", "D1", label="Retrieve Payroll Data")
    dfd1.edge("P3", "D3", label="Generate Paychecks")
    dfd1.edge("P4", "D1", label="Retrieve Payroll Data")
    dfd1.edge("P4", "D3", label="Store Payroll Reports")

    dfd1.edge("P3", "Employees", label="Paychecks")
    dfd1.edge("P4", "KRA", label="Tax Reports")
    dfd1.edge("P4", "Management", label="Payroll Reports")

    # Render
    dfd1.render("level_1_dfd_payroll", format="jpg", cleanup=True)

def generate_level_2():
    """Creates Level 2 DFD (Detailed Breakdown of Payroll Processing)"""
    dfd2 = Digraph("Level_2_DFD", format="jpg")

    # Processes in Payroll Processing
    dfd2.node("P3.1", "Validate Time Data", shape="ellipse", style="filled", fillcolor="lightgreen")
    dfd2.node("P3.2", "Calculate Gross Salary", shape="ellipse", style="filled", fillcolor="lightgreen")
    dfd2.node("P3.3", "Deduct Taxes & Contributions", shape="ellipse", style="filled", fillcolor="lightgreen")
    dfd2.node("P3.4", "Generate Paychecks", shape="ellipse", style="filled", fillcolor="lightgreen")

    # Data Stores
    dfd2.node("D1", "Payroll File", shape="cylinder", style="filled", fillcolor="lightgrey")
    dfd2.node("D3", "Payroll Reports", shape="cylinder", style="filled", fillcolor="lightgrey")

    # Connections
    dfd2.edge("D1", "P3.1", label="Retrieve Time Data")
    dfd2.edge("P3.1", "P3.2", label="Validated Time Data")
    dfd2.edge("P3.2", "P3.3", label="Gross Salary")
    dfd2.edge("P3.3", "P3.4", label="Net Salary")
    dfd2.edge("P3.4", "D3", label="Store Paychecks")
    dfd2.edge("P3.4", "Employees", label="Paychecks")

    # Render
    dfd2.render("level_2_dfd_payroll", format="jpg", cleanup=True)

# Generate all DFD levels
generate_level_0()
generate_level_1()
generate_level_2()

print("DFD images generated: level_0_dfd_payroll.jpg, level_1_dfd_payroll.jpg, level_2_dfd_payroll.jpg")
