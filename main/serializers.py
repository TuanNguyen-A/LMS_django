from rest_framework import serializers
from . import models 
from django.contrib.flatpages.models import FlatPage

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher 
        fields=['id','full_name','email','password','qualification', 'mobile_no', 'skills','profile_img', 'teacher_courses', 'skill_list']
    
    def __init__(self, *args, **kwargs):
        super(ChapterSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['total_teacher_courses', 'total_teacher_students','total_teacher_chapters']
    
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseCategory 
        fields=['id','title', 'description','total_courses']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Course 
        fields=['id','category', 'teacher','title','description', 'featured_img', 'techs', 'course_chapters', 'related_videos', 'tech_list', 'total_enrolled_student', 'course_rating']
    
    def __init__(self, *args, **kwargs):
        super(ChapterSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Chapter 
        fields=['id','course','title','description', 'video', 'chapter_duration','remarks']
    
    def __init__(self, *args, **kwargs):
        super(ChapterSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Student 
        fields=['id','full_name','email','password','username', 'interested_categories', 'profile_img']

class StudentCourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.StudentCourseEnrollment 
        fields=['id','course', 'student','enrolled_time']
    
    def __init__(self, *args, **kwargs):
        super(StudentCourseEnrollSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class StudentFavoriteCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.StudentFavoriteCourse()
        fields=['id','course', 'student','status']
    
    def __init__(self, *args, **kwargs):
        super(StudentFavoriteCourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseRating() 
        fields=['id','course', 'student','rating', 'reviews', 'review_time']
    
    def __init__(self, *args, **kwargs):
        super(ChapterSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2


class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Course 
        fields=['id', 'teacher','student','title', 'detail', 'add_time']
    
    def __init__(self, *args, **kwargs):
        super(StudentAssignmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1
    
class StudentDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['enrolled_courses', 'favorite_courses','complete_assignments', 'pending_assignments']
    
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Notification 
        fields=['teacher','student','notif_subject', 'notif_for']
    
    def __init__(self, *args, **kwargs):
        super(NotificationSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Quiz 
        fields=['id','teacher','title','detail', 'assign_status','add_time']
    
    def __init__(self, *args, **kwargs):
        super(QuizSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Question 
        fields=['id','quiz','ans1','ans2', 'ans3', 'ans4', 'right_ans']
    
    def __init__(self, *args, **kwargs):
        super(QuestionSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1


class CourseQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseQuiz 
        fields=['id','teacher','course', 'quiz','add_time']
    
    def __init__(self, *args, **kwargs):
        super(CourseQuizSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class AttemptQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AttemptQuiz 
        fields=['id','student','question','right_ans','add_time']
    
    def __init__(self, *args, **kwargs):
        super(AttemptQuizSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.StudyMaterial 
        fields=['id','course','title','description', 'upload', 'remarks']
    
    def __init__(self, *args, **kwargs):
        super(StudyMaterialSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.FAQ 
        fields=['id','question', 'answer']

class FlatPagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlatPage
        fields=['id','title','content', 'url']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Contact
        fields=['id','full_name','email', 'query_txt']

