from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        driver = self.app.driver
        if not driver.current_url.endswith("/manage_proj_page.php") and \
                len(driver.find_elements_by_xpath("//input[@value='Create New Project']")) == 0:
            driver.find_element_by_link_text("Manage").click()
            driver.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        driver = self.app.driver
        self.open_project_page()
        # init project creation
        driver.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        # submit project creation
        driver.find_element_by_css_selector("input[value='Add Project']").click()
        self.project_cache = None

    def fill_project_form(self, project):
        # driver = self.app.driver
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_project_by_index(self, index):
        # driver = self.app.driver
        self.open_project_page()
        self.select_project_by_index(index)
        # submit deletion
        self.click_delete()
        self.click_delete()
        self.project_cache = None

    def click_delete(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//input[@value='Delete Project']").click()

    def select_project_by_index(self, index):
        driver = self.app.driver
        driver.find_element_by_css_selector("a[href='%s']" % index).click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            self.open_project_page()
            self.project_cache = []
            self.find_selector('.width100 tr.row-2')
            self.find_selector('.width100 tr.row-1')
        return list(self.project_cache)

    def find_selector(self, cclass):
        driver = self.app.driver
        for element in driver.find_elements_by_css_selector(cclass):
            if element.find_element_by_tag_name('a'):
                href = element.find_element_by_tag_name('a').get_attribute('href')
                self.project_cache.append(Project(path=href[33:]))
