SELECT 
    company.company_code, 
    company.founder,
    COUNT(DISTINCT lead_manager.lead_manager_code),
    COUNT(DISTINCT senior_manager.senior_manager_code),
    COUNT(DISTINCT manager.manager_code),
    COUNT(DISTINCT employee.employee_code)
FROM 
    company
    JOIN lead_manager ON company.company_code = lead_manager.company_code
    JOIN senior_manager ON company.company_code = senior_manager.company_code
    JOIN manager ON company.company_code = manager.company_code
    JOIN employee ON company.company_code = employee.company_code
GROUP BY company.company_code, company.founder
ORDER BY company.company_code;
