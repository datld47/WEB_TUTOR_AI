from datetime import date

from django.shortcuts import render

all_posts=[
    {
       'slug':'hike-in-the-mountains',
       'image':'mountains.jpg',
       'author':'Max',
       'date': date(2021,7,21),
       'title':'Mountain Hiking',
       'excerpt':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quod soluta temporibus voluptatibus ex veniam eum, provident deserunt, voluptate rerum minus alias. Pariatur consectetur neque accusantium delectus impedit repellendus eaque odit.',
       'content':'''
       
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Blanditiis, suscipit nostrum. Quis excepturi, itaque ex iure, saepe distinctio quaerat sit nam fuga hic consectetur corrupti et, dolorum est dolore. Commodi mollitia dicta unde consequatur velit dolorem, at molestias sit alias et dolore minima omnis voluptas eius sequi quod id reiciendis nesciunt est animi consectetur. Amet voluptates qui nisi sit impedit. Animi a nam voluptatem eos officiis quas, accusamus cumque totam, sint dolore provident ipsam dolorem exercitationem explicabo. Accusantium iusto sapiente mollitia blanditiis magnam libero ab iure optio eveniet enim unde repellat veritatis a eius ratione, pariatur necessitatibus accusamus minima! Commodi?
        
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Blanditiis, suscipit nostrum. Quis excepturi, itaque ex iure, saepe distinctio quaerat sit nam fuga hic consectetur corrupti et, dolorum est dolore. Commodi mollitia dicta unde consequatur velit dolorem, at molestias sit alias et dolore minima omnis voluptas eius sequi quod id reiciendis nesciunt est animi consectetur. Amet voluptates qui nisi sit impedit. Animi a nam voluptatem eos officiis quas, accusamus cumque totam, sint dolore provident ipsam dolorem exercitationem explicabo. Accusantium iusto sapiente mollitia blanditiis magnam libero ab iure optio eveniet enim unde repellat veritatis a eius ratione, pariatur necessitatibus accusamus minima! Commodi?
         
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Blanditiis, suscipit nostrum. Quis excepturi, itaque ex iure, saepe distinctio quaerat sit nam fuga hic consectetur corrupti et, dolorum est dolore. Commodi mollitia dicta unde consequatur velit dolorem, at molestias sit alias et dolore minima omnis voluptas eius sequi quod id reiciendis nesciunt est animi consectetur. Amet voluptates qui nisi sit impedit. Animi a nam voluptatem eos officiis quas, accusamus cumque totam, sint dolore provident ipsam dolorem exercitationem explicabo. Accusantium iusto sapiente mollitia blanditiis magnam libero ab iure optio eveniet enim unde repellat veritatis a eius ratione, pariatur necessitatibus accusamus minima! Commodi?
       '''
    },
    
    {
       'slug':'progaming-is-fun',
       'image':'coding.jpg',
       'author':'Max',
       'date': date(2022,3,10),
       'title':'Proraming is Great',
       'excerpt':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quod soluta temporibus voluptatibus ex veniam eum, provident deserunt, voluptate rerum minus alias. Pariatur consectetur neque accusantium delectus impedit repellendus eaque odit.',
       'content':'''
       
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Blanditiis, suscipit nostrum. Quis excepturi, itaque ex iure, saepe distinctio quaerat sit nam fuga hic consectetur corrupti et, dolorum est dolore. Commodi mollitia dicta unde consequatur velit dolorem, at molestias sit alias et dolore minima omnis voluptas eius sequi quod id reiciendis nesciunt est animi consectetur. Amet voluptates qui nisi sit impedit. Animi a nam voluptatem eos officiis quas, accusamus cumque totam, sint dolore provident ipsam dolorem exercitationem explicabo. Accusantium iusto sapiente mollitia blanditiis magnam libero ab iure optio eveniet enim unde repellat veritatis a eius ratione, pariatur necessitatibus accusamus minima! Commodi?
        
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Blanditiis, suscipit nostrum. Quis excepturi, itaque ex iure, saepe distinctio quaerat sit nam fuga hic consectetur corrupti et, dolorum est dolore. Commodi mollitia dicta unde consequatur velit dolorem, at molestias sit alias et dolore minima omnis voluptas eius sequi quod id reiciendis nesciunt est animi consectetur. Amet voluptates qui nisi sit impedit. Animi a nam voluptatem eos officiis quas, accusamus cumque totam, sint dolore provident ipsam dolorem exercitationem explicabo. Accusantium iusto sapiente mollitia blanditiis magnam libero ab iure optio eveniet enim unde repellat veritatis a eius ratione, pariatur necessitatibus accusamus minima! Commodi?
         
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Blanditiis, suscipit nostrum. Quis excepturi, itaque ex iure, saepe distinctio quaerat sit nam fuga hic consectetur corrupti et, dolorum est dolore. Commodi mollitia dicta unde consequatur velit dolorem, at molestias sit alias et dolore minima omnis voluptas eius sequi quod id reiciendis nesciunt est animi consectetur. Amet voluptates qui nisi sit impedit. Animi a nam voluptatem eos officiis quas, accusamus cumque totam, sint dolore provident ipsam dolorem exercitationem explicabo. Accusantium iusto sapiente mollitia blanditiis magnam libero ab iure optio eveniet enim unde repellat veritatis a eius ratione, pariatur necessitatibus accusamus minima! Commodi?
       '''
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date, reverse=True)
    # Lấy 3 bài đăng mới nhất (top 3 sau khi sắp xếp giảm dần)
    latest_posts = sorted_posts[:3]
    return render(request,'blog/index.html',{"posts":latest_posts})

def posts(request):
    return render(request,"blog/all-posts.html",{"all_posts":all_posts})

def post_detail(request,slug):
    indentified_post=next(post for post in all_posts if post['slug']==slug)
    return render(request,"blog/post-detail.html",{'post':indentified_post})