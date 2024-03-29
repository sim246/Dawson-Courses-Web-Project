--calling table drops
@remove.sql

--removing indexes
@remove_indexes.sql

--adding objects
@project_type.sql

--Creating tables
--Term
create table terms (term_id number generated always as identity  PRIMARY KEY, 
                    term_name char(6) NOT NULL);

--Domain
create table domains (domain_id number generated always as identity PRIMARY KEY, 
                        domain varchar2(50) NOT NULL, 
                        domain_description varchar2(500) NOT NULL);

--Course
create table courses (course_id varchar2(10) PRIMARY KEY, 
                    course_title varchar2(50) NOT NULL,
                    theory_hours number NOT NULL, 
                    lab_hours number NOT NULL, 
                    work_hours number NOT NULL,
                    description varchar2(1000) NOT NULL, 
                    domain_id REFERENCES domains(domain_id) ON DELETE CASCADE, 
                    term_id REFERENCES terms(term_id));

--Competency
create table competencies (competency_id char(4) PRIMARY KEY, 
                            competency varchar2(250) NOT NULL,
                            competency_achievement varchar2(500) NOT NULL ,
                            competency_type varchar2(10) NOT NULL);
                        
--Element
create table elements (element_id number generated always as identity PRIMARY KEY, 
                        element_order number NOT NULL, 
                        element varchar2(250) NOT NULL,
                        element_criteria varchar2(500) NOT NULL, 
                        competency_id REFERENCES competencies(competency_id) ON DELETE CASCADE);
                    
--Courses_Elements (Bridging)
create table courses_elements (course_id REFERENCES courses(course_id) ON DELETE CASCADE, 
                                element_id REFERENCES elements(element_id) ON DELETE CASCADE, 
                                element_hours number NOT NULL);

--calling creation of the users table with instructor user.
@users.sql

--calling creation of sample data
@inserting.sql

--adding triggers for logging
@logging.sql

--adding views
@views.sql

--adding package
@courses_package.sql

--adding indexes
@indexes.sql


