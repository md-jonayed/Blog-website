from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

posts = [
    {"id": 1, "title": "Getting Started with Django",
        "content": """
        Learn how to set up your first Django project and understand its MTV architecture.
        Django is one of the most popular web development frameworks for Python, known for its simplicity, scalability, and "batteries-included" philosophy. If you're new to Django, setting up your first project might seem daunting at first, but it's actually a straightforward and rewarding process.

        To get started, you'll first need to install Django. The easiest way to do this is by using pip, Python’s package manager. Simply open your terminal and run pip install django. Once installed, you can verify the installation by running django-admin --version.

        Next, create your first Django project by executing the command django-admin startproject myproject. This will create a new directory called myproject containing all the basic files you need to start building your site. Inside this directory, you'll find important files like manage.py and a subdirectory also called myproject which holds settings, URLs, and WSGI configuration.

        Django follows the MTV architecture — which stands for Model-Template-View. This is similar to the popular MVC pattern but adapted to Django’s way of thinking:

        Model: Represents the data layer. Models define the structure of your database and how your data will be managed.

        Template: Deals with the presentation layer. Templates control how your website will look by combining HTML with Django's template language.

        View: Manages the logic. Views are Python functions or classes that process requests and return responses.

        When a user interacts with your website, Django uses its powerful URL dispatcher to route the request to the appropriate view. The view fetches data from the model (if needed), passes it to a template, and finally renders a complete HTML page for the user.

        Once your project is created, you’ll often want to create Django "apps" inside it. Think of an app as a module that handles one piece of the website’s functionality, like a blog, a user authentication system, or an e-commerce cart. You can create an app using the command python manage.py startapp myapp.

        From there, you will register your app in the project's settings.py, define models, set up views, configure URLs, and create templates to present the data beautifully. Django's admin interface also allows you to manage your database entries easily without writing complex queries.

        With Django, you’re able to move quickly from an idea to a fully functional web application. Whether you are building a simple blog or a high-traffic website, Django’s robust framework ensures that you can focus more on building your app and less on reinventing the wheel.
        """},
    {"id": 2, "title": "Python Tips and Tricks",
        "content": """
        Boost your Python productivity with these essential tips and tricks.
        Python is often praised for its simplicity and readability, but even seasoned developers can find ways to write better, more efficient code by mastering a few handy tips and tricks. Whether you're a beginner or a more experienced programmer, these insights can help boost your productivity and make your Python code more elegant.

        One essential tip is to use list comprehensions whenever possible. Instead of writing a few lines to create and populate a list, you can do it all in one line:

        python
        squares = [x * x for x in range(10)]
        This not only saves lines but also makes your intentions clear to anyone reading your code.

        Another trick is mastering the power of enumerate() and zip(). When you need both the index and the value from a list, use enumerate() instead of manually managing a counter. Similarly, zip() allows you to iterate over two lists at once, pairing corresponding elements.

        For handling missing dictionary keys gracefully, Python’s dict.get() method is a lifesaver. Instead of risking a KeyError, you can provide a default value:

        python
        my_dict.get('key', 'default_value')
        Python’s unpacking feature is another underrated gem. You can unpack lists, tuples, and even dictionaries neatly:

        python

        a, b, *rest = [1, 2, 3, 4, 5]
        Here, a is 1, b is 2, and rest becomes [3, 4, 5].

        When writing functions, using *args and **kwargs allows you to create highly flexible APIs, making your functions adaptable to a variety of inputs.

        Another productivity booster is using f-strings (available in Python 3.6+). Instead of cumbersome concatenation or format() calls, f-strings allow you to embed expressions inside string literals with minimal effort:

        python
        name = "Alice"
        print(f"Hello, {name}!")
        In terms of debugging, the built-in pdb library is incredibly useful. Inserting import pdb; pdb.set_trace() into your code lets you pause execution and explore variable states interactively.

        Finally, writing clean Python is not just about shorter syntax. Embrace Python's philosophy of "There should be one– and preferably only one –obvious way to do it." Follow PEP 8 style guidelines, use meaningful variable names, and structure your code clearly. Remember, code is read much more often than it is written.

        By incorporating these tips and continuously exploring Python’s vast ecosystem, you can dramatically improve your programming efficiency and enjoy an even smoother development experience.
"""
     },
    {"id": 3, "title": "The Basics of Artificial Intelligence",
        "content": """
        Understand what AI is and explore its main applications in the modern world.
        Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems. It’s an expansive field that covers everything from basic rule-based systems to complex deep learning networks capable of learning and evolving.

        At its core, AI is all about enabling machines to perform tasks that typically require human intelligence. These tasks include understanding natural language, recognizing patterns, solving problems, making decisions, and even learning from experience.

        There are two broad categories of AI: Narrow AI and General AI. Narrow AI refers to systems that are designed to perform a specific task, such as a chatbot answering customer queries or a recommendation engine suggesting movies. Most AI applications we see today fall into this category. General AI, on the other hand, refers to machines that can perform any intellectual task a human can do. This type of AI remains largely theoretical and is the subject of intense research.

        Some key applications of AI include:

        Natural Language Processing (NLP): Enabling machines to understand and generate human language. Applications include virtual assistants like Siri or Alexa, and tools like chatbots.

        Computer Vision: Allowing machines to interpret and make decisions based on visual input. This technology powers facial recognition, medical imaging analysis, and self-driving car vision systems.

        Expert Systems: AI systems that use a database of expert knowledge to offer advice or diagnose problems.

        Robotics: AI is integrated into robots to allow them to perform tasks ranging from industrial manufacturing to surgery.

        Recommendation Systems: Netflix, Amazon, and Spotify use AI to recommend products, shows, and music tailored to your preferences.

        The main technologies behind AI include machine learning, deep learning, neural networks, and reinforcement learning. Machine learning, for instance, allows computers to learn patterns from data without being explicitly programmed for every scenario.

        Despite its massive benefits, AI also raises concerns about job automation, ethics, and biases. It's important for developers and society as a whole to build AI systems responsibly.

        In the coming years, AI will become even more deeply integrated into our lives. Understanding its basics is essential not just for tech professionals but for anyone who interacts with technology today.

        """

     },
    {"id": 4, "title": "Machine Learning 101",
        "content": """
        Dive into the basics of machine learning, including types, algorithms, and real-world use cases.
        Machine Learning (ML) is a branch of Artificial Intelligence that focuses on building systems capable of learning from data without being explicitly programmed for every possible scenario. Instead of relying on fixed rules, machine learning models identify patterns, make decisions, and improve over time with more data.

        At a high level, machine learning involves feeding large amounts of data into algorithms, which then produce models capable of making predictions or decisions based on new inputs. For example, a machine learning model could learn to recognize spam emails by studying thousands of examples.

        There are three main types of machine learning:

        Supervised Learning: In this type, the algorithm is trained on labeled data. Each training example includes the input data and the correct output. Tasks like classification (e.g., recognizing handwritten digits) and regression (e.g., predicting house prices) fall into this category.

        Unsupervised Learning: Here, the data isn’t labeled. The system tries to learn the underlying structure without explicit guidance. Clustering (e.g., customer segmentation) and dimensionality reduction (e.g., principal component analysis) are common tasks.

        Reinforcement Learning: In this approach, an agent learns to make decisions by taking actions in an environment and receiving feedback in the form of rewards or penalties. Applications include game AI (like AlphaGo) and robotics.

        Some key algorithms you might encounter in machine learning include:

        Linear Regression for predicting continuous values.

        Decision Trees and Random Forests for classification.

        Support Vector Machines (SVM) for finding optimal decision boundaries.

        K-Means Clustering for grouping similar data points.

        Neural Networks for more complex tasks like image and speech recognition.

        Real-world use cases for machine learning are everywhere. It powers personalized recommendations on Netflix, fraud detection systems in banks, speech recognition on smartphones, medical diagnosis tools, and even autonomous vehicles.

        Learning machine learning also involves understanding concepts like overfitting, underfitting, training/test splits, cross-validation, and evaluation metrics like accuracy, precision, recall, and F1-score.

        With the explosion of available data and powerful computational resources, machine learning is becoming an indispensable tool across industries. A solid grasp of ML fundamentals opens the door to countless exciting possibilities!


        """},
    {"id": 5, "title": "Getting Started with Android Development",
        "content": """
        Learn how to build your first Android app using Java or Kotlin.
        Android development is one of the most exciting fields in software engineering today. With billions of active Android devices worldwide, learning how to build apps for this ecosystem opens countless opportunities.

        The first step to Android development is choosing your language: Java and Kotlin are the two official languages. Java has been around longer and is extremely widespread, while Kotlin is modern, concise, and fully supported by Google as a first-class language for Android apps.

        To start building Android apps, you’ll need to set up Android Studio, the official integrated development environment (IDE). Android Studio provides powerful tools for writing code, designing interfaces, managing project structure, debugging, and testing your applications.

        Your first Android project will follow a basic structure:

        Manifest File (AndroidManifest.xml): This file declares essential information about your app, like its components, permissions, and hardware features.

        Activities: Each screen or UI in an Android app is represented by an Activity. Activities manage the user interface and handle user interaction.

        Layouts: Layouts (XML files) define how UI elements like buttons, text fields, and images are organized on the screen.

        Resources: Resources such as strings, images, and styles are kept separate from the code to support localization and easier updates.

        A simple Android app usually begins with creating a new Activity and linking it to a Layout. You write the app’s logic inside the Activity in Java or Kotlin, and design the UI using XML.

        Understanding the Activity lifecycle is crucial for creating responsive, memory-efficient apps. Each activity passes through states like onCreate(), onStart(), onResume(), and so on.

        As you grow more comfortable, you'll dive into more advanced concepts such as:

        Fragments (modular sections of UI)

        RecyclerViews (for efficiently displaying lists)

        Intents (for communication between activities)

        Services (for background operations)

        Firebase Integration (for backend services like authentication, databases, and push notifications)

        Android app development also involves testing, performance optimization, and publishing your app to the Google Play Store.

        The journey of building Android apps is creative, challenging, and immensely rewarding. With consistent practice and a focus on user-centered design, you can build apps that impact millions!


        """},
    {"id": 6, "title": "Introduction to Java Programming",
        "content": """
        Explore Java fundamentals including OOP principles, syntax, and simple programs.
        Java is one of the most popular and widely used programming languages in the world, known for its portability, robustness, and strong community support. It follows the Object-Oriented Programming (OOP) paradigm, emphasizing concepts like classes, objects, inheritance, polymorphism, abstraction, and encapsulation.

        Setting up Java is straightforward. Install the Java Development Kit (JDK) and use a simple IDE like Eclipse or IntelliJ IDEA to start writing code.

        A basic Java program looks like this:

        public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello, World!");
            }
        }
        The main method is the entry point of any Java application. Java programs are compiled into bytecode that runs on the Java Virtual Machine (JVM), making them platform-independent — "write once, run anywhere."

        Important features of Java include:

        Strong Typing: Every variable must be declared with a type (e.g., int, String, boolean).

        OOP Principles: Java is built around the idea of classes and objects. A class is a blueprint, and an object is an instance of a class.

        Memory Management: Java has automatic garbage collection, which helps manage memory and clean up unused objects.

        Exception Handling: Java has robust mechanisms (try, catch, finally) for dealing with errors gracefully.

        As you advance, you'll encounter key concepts like:

        Interfaces and Abstract Classes for flexible software design

        Collections Framework (ArrayList, HashMap, HashSet) for managing groups of objects

        Multithreading for concurrent programming

        Generics for type-safe operations on objects

        Java is used for building Android apps, web applications (with frameworks like Spring), desktop applications, and enterprise systems.

        Mastering Java fundamentals gives you a strong foundation to explore more complex fields like Android development, server-side programming, or large-scale system architecture.
        """},
    {"id": 7, "title": "Understanding Data Structures",
        "content": """
        Learn about arrays, linked lists, stacks, queues, trees, and graphs.
        Data structures are fundamental to computer science and software engineering. They are ways to organize, manage, and store data efficiently for access and modification. Knowing when and how to use the right data structure can make your programs faster, cleaner, and easier to maintain.

        Let's look at some common data structures:

        Arrays: Fixed-size, contiguous memory locations storing elements of the same type. Great for indexing but poor for insertions and deletions.

        Linked Lists: Consist of nodes where each node contains data and a reference to the next node. They allow efficient insertions and deletions but slower access times compared to arrays.

        Stacks: Follow a Last In, First Out (LIFO) principle. Imagine a stack of plates — you add to the top and remove from the top.

        Queues: Follow a First In, First Out (FIFO) principle. Like a line of people waiting — the first to arrive is the first to be served.

        Trees: Hierarchical data structures where each node has a value and references to child nodes. Special types include Binary Trees, Binary Search Trees (BST), and Heaps.

        Graphs: A collection of nodes (vertices) connected by edges. Useful for representing networks like social connections or city maps.

        Choosing the right data structure depends on your problem. For example:

        Use a stack to implement undo features.

        Use a queue for task scheduling.

        Use a hash map for fast lookup.

        Use a tree for hierarchical data like file systems.

        Understanding Big O Notation is essential when working with data structures. It describes the worst-case performance in terms of time and space complexity.

        Learning data structures not only improves your coding efficiency but also prepares you for technical interviews where you might be asked to solve problems under time constraints.


        """},
    {"id": 8, "title": "Algorithm Basics",
        "content": """
        Understand common algorithms like sorting, searching, and recursion.
        Algorithms are step-by-step procedures or formulas for solving problems. They form the backbone of computer science, enabling computers to perform tasks ranging from simple calculations to complex data analysis.

        Several fundamental types of algorithms include:

        Sorting Algorithms: Organize data into a particular order. Examples include Bubble Sort, Merge Sort, Quick Sort, and Insertion Sort. Knowing their time complexity (like O(n log n) for Merge Sort) is crucial.

        Searching Algorithms: Locate an element in a data structure. Linear Search and Binary Search are classic examples.

        Recursive Algorithms: Solve a problem by breaking it down into smaller instances of the same problem. Famous recursive problems include calculating factorials, solving the Tower of Hanoi, or navigating tree structures.

        Greedy Algorithms: Build up a solution piece by piece, always choosing the next piece that offers the most immediate benefit (e.g., coin change problem, Prim’s algorithm for Minimum Spanning Tree).

        Dynamic Programming: Break problems into overlapping subproblems and solve each once, storing the solutions for efficiency. Examples include the Fibonacci sequence and the Knapsack problem.

        Backtracking Algorithms: Try out all possibilities and "backtrack" when a solution path fails. Useful for puzzles like Sudoku.

        Understanding algorithms involves both designing them and analyzing their efficiency using Big O Notation, which measures how execution time grows with input size.

        Mastering basic algorithms provides the foundation for solving complex, real-world problems efficiently and elegantly.
        """},
    {"id": 9, "title": "Getting Started with C++",
        "content": """
        A beginner's guide to C++ covering syntax, variables, control structures, and functions.
        C++ is a powerful, high-performance programming language often used in systems programming, game development, and applications requiring real-time processing.

        Learning C++ begins with understanding its syntax and basic building blocks:

        #include <iostream>
        using namespace std;

        int main() {
            cout << "Hello, World!" << endl;
            return 0;
        }
        C++ supports both procedural and object-oriented programming. Core concepts include:

        Variables and Data Types: int, char, float, double, bool.

        Control Structures: if-else, loops (for, while, do-while), switch-case.

        Functions: Modularizing code into reusable blocks.

        Classes and Objects: Implementing encapsulation and inheritance.

        Key C++ features include:

        Pointers: Variables that store memory addresses. Pointers allow direct memory access, which is powerful but needs careful handling.

        Memory Management: C++ requires manual memory management using new and delete.

        Templates: Write generic and reusable code.

        STL (Standard Template Library): A powerful library offering collections like vectors, stacks, queues, and maps.

        C++ is widely used where performance and control over hardware are critical. Whether building video games, operating systems, or high-frequency trading platforms, C++ remains a crucial skill.

        Mastering C++ fundamentals opens the door to understanding lower-level system concepts and advanced computer science topics.


        """}
]

# posts=""


def home(request):
    html = ""
    for post in posts:
        html = html + f"""
        <div>
        <a href="/posts/{post['id']}/">
        <h3>{post['id']}: {post['title']}</h3>
        </a>
        <p><b>{post['content']}</b></p>
        </div>
        """
    return render(request, 'posts/home.html', {'posts': posts})


def post(request, postId):
    for post in posts:
        if postId == post['id']:
            postDict = post
            break
        else:
            postDict = None
    if postDict:
        html = f"""
        <div>
        <h3><u>{postDict['title']}</u></h3>
        <p><b>{postDict['content']}</b></p>
        </div>
"""
        return render(request, 'posts/post.html', {'post': postDict})
    else:
        return HttpResponseNotFound("<h1>Post not found</h1>")


def redirectToPost(request, postId):
    url = reverse("post", args=[postId])
    return HttpResponseRedirect(url)


def contact(request):
    return render(request, 'posts/contact.html')
