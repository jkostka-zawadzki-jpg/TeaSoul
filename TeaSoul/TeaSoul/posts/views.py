from django.views.generic import DetailView, ListView

from .models import Category, Post, Topic


class CategoryListView(ListView):
    model = Category
    context_object_name = "categories"
    template_name = "posts/category_list.html"


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = "category"
    template_name = "posts/category_detail.html"


class TopicListView(ListView):
    model = Topic
    context_object_name = "topics"
    template_name = "posts/topic_list.html"


class TopicDetailView(DetailView):
    model = Topic
    context_object_name = "topic"
    template_name = "posts/topic_detail.html"


class TopicPostListView(ListView):
    context_object_name = "posts"
    template_name = "posts/topic_posts.html"

    def get_queryset(self):
        return (
            Post.objects.select_related("topic", "topic__category", "created_by")
            .filter(topic_id=self.kwargs["pk"])
            .order_by("-created_at")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic"] = Topic.objects.select_related("category").get(
            pk=self.kwargs["pk"]
        )
        return context


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "posts/post_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"
