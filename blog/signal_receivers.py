from tags.models import TaggedItem, Tag
from django.contrib.contenttypes.models import ContentType 

def create_tags(sender, instance, created, **kwargs):
    terms = str(instance.tag).split(',')
    if ',' in terms:
        terms = [term.strip() for term in terms]
    terms = list(filter(('').__ne__, terms))
    terms = list(filter((',').__ne__, terms))
    tags = []
    print(terms)
    for term in terms:
        tag_object = Tag.objects.filter(label=term).first()
        if not tag_object:
            tag = Tag(label=term)
            tag.save()
            tags.append(tag)
        else:
            tags.append(tag_object)

    content_type = ContentType.objects.get_for_model(sender)
    tagged_item_objects = TaggedItem.objects.filter(content_type=content_type,
                                            object_id = instance.id)
    for tagged_item in tagged_item_objects:
        tagged_item.delete()

    for tag in list(set(tags)):   
        print(tag)   
        tagged_item = TaggedItem(content_type=content_type,
                                object_id=instance.id, tag=tag)
        tagged_item.save()